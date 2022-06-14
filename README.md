# Course work №3
[link to the source](https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2)
### Task:

|![the-kat](https://skyengpublic.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbb8c2d8f-7405-4704-9ba3-0770d8390c54%2FUntitled.png?table=block&id=0ba38779-0629-4158-ba7d-0db2a83a9016&spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&width=670&userId=&cache=v2)|**Hi, this is Joni Catsville** and today we are going to create our Instagram with food, cats and more food! <br/><br/>This coursework requires knowledge of HTML, Flask, Jinja and of course Python. |
| :--: | :-- |
---
![the-app](https://skyengpublic.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F535dde70-367d-4cc4-821d-5a826159f876%2F2022-04-01_14.53.48.gif?table=block&id=94d77747-75f1-487f-b5fb-c76782d4b33e&spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&userId=&cache=v2)

---

|`IMPORTANT!` Complete all previous homework and only then proceed to the coursework.|
| :---: |

## Project Description
### Feed
List of posts. Should be displayed:
- author
- short text (50 characters)
- number of views
- Link to post.

Link to bookmarks in the header.

[Link to the Figma project - list of posts](https://www.figma.com/file/SNcwz5Ri8eHj0dF2QUiGyq/python_backend_008_projects?node-id=79%3A63)

### Detailed post
The post details page should have content:
* Photo
* Text
* Author's card (from these "posts").
* Comments (from a file with comments).
* Link "Back" to the main page

[Link to the Figma project - detailed post](https://www.figma.com/file/SNcwz5Ri8eHj0dF2QUiGyq/python_backend_008_projects?node-id=79%3A491)

### Search
The search form is activated by pressing Enter. The search results are then displayed.

[Link to the Figma project - search](https://www.figma.com/file/SNcwz5Ri8eHj0dF2QUiGyq/python_backend_008_projects?node-id=79%3A656)

### All user posts (star version)
* Selected user's posts sorted by date and time.
* The back button takes you back to the main page.

[Link to the Figma project - user posts](https://www.figma.com/file/SNcwz5Ri8eHj0dF2QUiGyq/python_backend_008_projects?node-id=79%3A608)

### Posts by tag (star version)
* A hashtag is a link in the text of a post, it leads to a page with all the posts where this hashtag occurs.
* The back button takes you back to the main page.

[Link to the Figma project - hashtags](https://www.figma.com/file/SNcwz5Ri8eHj0dF2QUiGyq/python_backend_008_projects?node-id=79%3A549)

### Bookmarks (star version)
* The page where all marked posts
* You can delete posts from the page.
* The back button takes you to the main page.

[Link to the Figma project - bookmarks](https://www.figma.com/file/SNcwz5Ri8eHj0dF2QUiGyq/python_backend_008_projects?node-id=79%3A323)

## Implementation
### Preparation
#### 1. Fork the repository to your github account: [https://github.com/skypro-008/coursework2_source](https://github.com/skypro-008/coursework2_source)
there is a list of posts, pictures, HTML templates, and CSS styles.
#### 2. Move the templates to the `templates` folder.
#### 3. Move the styles and pictures to the `static` folder.
`Please note:` the data is stored separately. Posts with information about the author and his profile picture are stored in the `posts.json` file, comments are stored in the `comments.json` file. A bookmarks.json file is also stored with bookmarks data.
#### 4. Each post contain:
* `poster_name` — name/username of the post author.
* `poster_avatar` — post author's avatar.
* `pic` - post picture.
* `content` - post text.
* `views_count` - number of views.
* `likes_count` - number of likes.
* `pk` - id or post number.

Please note that the number of comments is not specified!

#### 5. Each comment contain:
* `post_id` - "post" identifier
* `commenter_name` - commenter name
* `comment` – comment text
* `pk` - identifier (number) comment

### Step 0 - prepare the functions

Before implementing a Flask application, you must write the data handling functions and put them in a separate file, such as `utils.py`. For example:
* `get_posts_all()` - returns posts
* `get_posts_by_user(user_name)` - returns the posts of a specific user. The function should raise `ValueError` if there is no such user, and an empty list if the user has no messages.
* `get_comments_by_post_id(post_id)` - returns comments for a specific post. The function should raise `ValueError` if there is no such entry, and an empty list if the entry has no comments.
* `search_for_posts(query)` - returns a list of posts by keyword
* `get_post_by_pk(pk)` - returns one post by its id.

Write unit tests for each function, put the tests in a separate `/tests` folder.
Organize tests as classes or functions as you wish.

### Step 1 - implement a posts feed
Create a view for all posts, this should be the main page.
`GET` `/`
* It should show all posts. 
* Use the right template. 
* Replace the paths to the style file and pictures in each template. (/`static/img` and `/static/css`)

### Step 2 - implement post detail view
* Create a view for a single post (`GET /posts/<postid>`)
* Get comments from `comments.json` by `postid`.
* Display comments for a post.
* `Do not process tags` - you will do this in one of the following steps.

### Step 3 - implement the search
* Create view for route search `GET /search/?s=...`
* Must display 10 posts or less.
* The search must be proceed by the substring in the text post. You can use low/upper case conversion or not.
* Use the correct pattern.

### Step 4 - Implement User post feed
Create a view displaying the posts of a specific user `GET /users/<username>`. Show posts by `username` from the query. Use the `user-feed` template

### Step 5 - Add Error Handlers

* Add a request handler to non-existent pages like `/meow` and return a 404 status code in this case.
* Add a server-side error handler (error 500, Internal Server Error ) and return status code 500.

### Step 6 - implement 2 API Endpoints
* Create a view that handles a `GET /api/posts` request and returns the full list of posts as a JSON list.
* Create a view that handles a `GET /api/posts/<post_id>` request and returns a single post as a JSON dictionary.

### Step 7 - implement logging to API endpoints
Use standard logging, logs should be stored in the logs folder in the `api.log` file. The log format should be like this:
```python
%(asctime)s [%(levelname)s] %(message)s
```
Example:
```python
2022-03-18 18:48:56 [INFO]Request /api/posts
2022-03-18 18:48:57 [INFO]Request /api/posts
2022-03-18 18:48:58 [INFO]Request /api/posts/2
2022-03-18 18:48:59 [INFO]Request /api/posts/3
```

### Step 8: Add an API Test

Test the `GET /api/posts` endpoint:
- returns a list
- elements have correct keys

Don't check the number of elements in the list as it may change

Test the `GET /api/posts/<post_id>` endpoint:
- returns a dict
- element have correct keys

Don't check the data in the resulting dictionary, it's not necessary.

## Hints:
To display a line in the template that contains HTML tags, tagline {{ content|safe }} is a special syntax that allows you to display tags without escaping them

## Additional task with a star
### Step 1 - Implement tag navigation

Add some code to the view that renders the post. Find words in the text of the post, select those that start with `#` and turn their links like `#food` >>> `<a href="/tag/food">#food</a>`

Create a view for `/tag/<tagname>.` In the list of posts, look for posts that contain a tag that starts with a pound sign. Output them in the right template

### Step 2 - bookmark posts.

* Create a view for adding bookmarks in the `bookmarks/add/postid` route. (Store bookmarks in bookmarks.json.)
* Redirect to the main page. (`/`) (use return redirect("address",code=302) in view)
* Create a view to remove from bookmarks in the `bookmarks/remove/postid` route.
* After deleting a bookmark, redirect to the main page (`/`)

### Step 3 - display bookmarks

Add a `/bookmarks` view, show all bookmarked posts. Take data from `bookmarks.json`.

## What will be checked in the coursework:
- [ ] Processing form data is done correctly
- [ ] Unfiltered list output is correct
- [ ] Filtered list output is correct
- [ ] Working with data is moved to a function or a separate class
- [ ] Data is filtered before being sent to the template, extra data is not transferred to the template

# Project status

Create MVP

# Some graphical information about project
[My Miro board](https://miro.com/app/board/uXjVOtUXZnM=/?share_link_id=994454813141)
