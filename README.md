"# Blogging_Platform_API"

## API Endpoints

### User Endpoints
- **POST `/register/`**  
  - **Request**: 
    ```json
    {"username": "string", "password": "string"}
    ```  
  - **Response**: 
    ```json
    {"message": "User registered successfully", "user_id": "integer"}
    ```

- **POST `/login/`**  
  - **Request**: 
    ```json
    {"username": "string", "password": "string"}
    ```  
  - **Response**: 
    ```json
    {"message": "Login successful", "token": "string"}
    ```

- **GET `/users/`**  
  - **Response**: 
    ```json
    [{"id": "integer", "username": "string"}, ...]
    ```

- **PUT `/update/<int:user_id>`**  
  - **Request**: 
    ```json
    {"username": "string", "password": "string"}
    ```  
  - **Response**: 
    ```json
    {"message": "User updated successfully"}
    ```

- **POST `/logout/`**  
  - **Response**: 
    ```json
    {"message": "Logout successful"}
    ```

### Blog Endpoints
- **POST `/create/`**  
  - **Request**: 
    ```json
    {"title": "string", "content": "string"}
    ```  
  - **Response**: 
    ```json
    {"message": "Blog post created successfully", "post_id": "integer"}
    ```

- **GET `/details/<int:id>/`**  
  - **Response**: 
    ```json
    {"id": "integer", "title": "string", "content": "string"}
    ```

- **PUT `/update/<int:id>/`**  
  - **Request**: 
    ```json
    {"title": "string", "content": "string"}
    ```  
  - **Response**: 
    ```json
    {"message": "Blog post updated successfully"}
    ```

- **DELETE `/delete/<int:id>/`**  
  - **Response**: 
    ```json
    {"message": "Blog post deleted successfully"}
    ```

- **GET `/list/`**  
  - **Response**: 
    ```json
    [{"id": "integer", "title": "string"}, ...]
    ```

- **DELETE `/tag/delete/<int:id>/`**  
  - **Response**: 
    ```json
    {"message": "Tag deleted successfully"}
    ```

- **POST `/category/create/`**  
  - **Request**: 
    ```json
    {"name": "string"}
    ```  
  - **Response**: 
    ```json
    {"message": "Category created successfully", "category_id": "integer"}
    ```

- **GET `/search/`**  
  - **Request**: 
    ```json
    {"query": "string"}
    ```  
  - **Response**: 
    ```json
    [{"id": "integer", "title": "string"}, ...]
    ```

- **GET `/filter/`**  
  - **Response**: 
    ```json
    [{"id": "integer", "title": "string"}, ...]
    ```
