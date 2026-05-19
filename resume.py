from python import resume_pb2
def create_resume():
    resume = resume_pb2.Resume()
    resume.name = "John Doe"
    resume.email = "john.doe@example.com"
    return resume

if __name__ == "__main__":              
    resume = create_resume()
    print(resume)
    
    
    
    
    
    