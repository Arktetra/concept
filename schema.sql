CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    mobile VARCHAR(15),
    role VARCHAR(50)
);

CREATE TABLE Posts (
    post_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INT NOT NULL,
    metaTitle VARCHAR(255),
    published_at TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES Users(user_id)
);

-- Create a function to update the updated_at column
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Add a trigger to the Posts table
CREATE TRIGGER set_updated_at
BEFORE UPDATE ON Posts
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TABLE Tags (
    tag_id SERIAL PRIMARY KEY,
    tag_name VARCHAR(100) NOT NULL,
    post_id INT NOT NULL,
    content TEXT,
    FOREIGN KEY (post_id) REFERENCES Posts(post_id)
);

CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    post_id INT NOT NULL,
    description TEXT,
    FOREIGN KEY (post_id) REFERENCES Posts(post_id)
);

CREATE TABLE Comments (
    comment_id SERIAL PRIMARY KEY,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES Posts(post_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Insert dummy values
INSERT INTO Users (user_name, email, password, mobile, role) 
VALUES ('John Doe', 'john.doe@example.com', 'securepassword', '1234567890', 'author');

INSERT INTO Posts (title, content, author_id, metaTitle, published_at) 
VALUES ('Sample Post', 'This is a sample post content.', 1, 'Sample Meta Title', NOW());

INSERT INTO Tags (tag_name, post_id, content) 
VALUES ('Sample Tag', 1, 'Tag content for the sample post.');

INSERT INTO Categories (category_name, post_id, description) 
VALUES ('Sample Category', 1, 'Description of the sample category.');

INSERT INTO Comments (post_id, user_id, comment_text) 
VALUES (1, 1, 'This is a sample comment.');
