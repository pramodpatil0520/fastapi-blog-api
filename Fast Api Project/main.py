from fastapi import FastAPI , Depends , HTTPException , Query
from sqlalchemy.orm import Session
from database import engine , SessionLocal
import models , schemas
from auth import create_token,verify_token

models.Base.metadata.create_all(bind=engine)

app = FastAPI ()

# DB Dependancy 

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close ()

# Login Api 

@app.post("/login")

def login():
    return {
        "access_token" : create_token({"user" : "admin"}),
        "token_type" : "bearer"
    }

#home 

@app.get("/")

def home():
    return {
        "message":"Blog api Started"
    }

# create blog (Protected)

@app.post("/blogs",response_model=schemas.BlogResponse)

def create_blogs(blogs:schemas.BlogCreate , db:Session = Depends(get_db) , user = Depends(verify_token)):
    new_blogs = models.Blog(
        title = blogs.title,
        content = blogs.content

    )

    db.add(new_blogs)
    db.commit()
    db.refresh(new_blogs)
    return new_blogs

# Read All Blogs 

@app.get("/blogs")

def get_blogs(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=5, ge=1, le=100),
    search: str = Query(default=""),
    db: Session = Depends(get_db)
):
    
    query = db.query(models.Blog)
    if search:
        query = query.filter(models.Blog.title.ilike(f"%{search}%")) 
    total = query.count()
    start = (page-1)*limit
    blogs = query.offset(start).limit(limit).all()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": (total + limit - 1) // limit,
        "data": blogs
    }
    

# React One Blog 

@app.get("/blogs/{id}",response_model=schemas.BlogResponse)

def get_blog(id : int,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()

    if not blog:
        raise HTTPException (status_code=404,detail="blog not found")

    return blog

# Update Blog Api 

@app.put("/blogs/{id}",response_model=schemas.BlogResponse)

def update_blog(id : int,blog:schemas.BlogCreate,db : Session = Depends(get_db) , user = Depends(verify_token)):
    existing_blog= db.query(models.Blog).filter(models.Blog.id==id).first()
    if not existing_blog:
            raise HTTPException (status_code=404,detail="blog not found")

    existing_blog.title=blog.title
    existing_blog.content=blog.content

    db.commit()
    
    return existing_blog

# Delete Blog Api 

@app.delete("/blogs/{id}")

def delete_blog(id:int,db : Session=Depends(get_db) , user = Depends(verify_token)):
    blog = db.query(models.Blog).filter(models.Blog.id == id )
    if not blog.first():
        raise HTTPException (status_code=404,detail="blog not found")

    blog.delete()
    db.commit()

    return {
        "message": " Blog is delete sucessfully "
    }