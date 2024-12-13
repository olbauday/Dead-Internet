import json
import random
from google.generativeai import GenerativeModel, configure
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv
load_dotenv()

class ReaperEngine:
    def __init__(self):
        configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = GenerativeModel("gemini-2.0-flash-exp") # Changed model name here
        self.internet_db = dict()
        self.temperature = 2.1
        self.max_tokens = 4096
        self.system_prompt = "You are an expert in creating realistic HTML, CSS, and Javascript webpages. You do not create sample pages, instead you create webpages that are completely realistic and look as if they really existed on the web. You do not respond with anything but HTML, starting your messages with <!DOCTYPE html> and ending them with </html>. If a requested page is not a HTML document, for example a CSS or Javascript file, write that language instead of writing any HTML. If the requested page is instead an image file or other non-text resource, attempt to generate an appropriate resource for it instead of writing any HTML. You use very little to no images at all in your HTML, CSS or JS."
        self.posts = {}
        self.home_page = self._get_index_html()
    
    def generate_posts(self, amount=5):
        posts = {}
        for i in range(amount):
            prompt = f"Generate a Reddit post, including a title, some text content, subreddit name, a unique url, author name, and engagement metrics (upvotes, comments). Do not use any html tags. Generate a unique URL for each post and do not return the url in a list. Return each element on a new line, and make sure that the URL does not start with a '/'. make sure time is in the format of 'x hours ago', 'x minutes ago', 'x days ago'. The format is: title\\ntext\\nsubreddit\\nurl\\nauthor\\ntime\\nupvotes\\ncomments"
            
            post_completion = self.model.generate_content(
              [prompt]
             )
            
            post_content = post_completion.text.split("\n")
            try:
                post = {
                    "title": post_content[0],
                    "text": post_content[1],
                    "subreddit": post_content[2],
                    "link": f"/r/{post_content[2]}/{post_content[3]}",
                    "author": post_content[4],
                    "time": post_content[5],
                    "upvotes": random.randint(0, 1000),
                    "comments": random.randint(0, 500),
                    "comments_list": [],
                }
                posts[f"{post_content[2]}/{post_content[3]}"] = post
            except:
                post = {
                    "title": "Error Generating Title",
                    "text": "Error Generating Text",
                    "subreddit": "error",
                    "link": f"/r/error/error",
                    "author": "error",
                    "time": "0 seconds ago",
                    "upvotes": 0,
                    "comments": 0,
                    "comments_list": [],
                }
        self.posts = posts
        return posts
    
    def _get_index_html(self):
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dead Internet Reddit</title>
    <style>
         body {
            font-family: 'Arial', sans-serif;
            margin: 20px;
            background-color: #f8f9fa;
            color: #343a40;
        }
        .container {
            width: 80%;
            margin: 0 auto;
        }
        .post {
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
        }
        .post h2 {
            margin-top: 0;
        }
        .post p {
            margin-bottom: 10px;
        }
        .post a {
            color: #007bff;
            text-decoration: none;
        }
         #header-bar {
          position: absolute;
          display: block;
          left: 0;
          right: 0;
          line-height: 30px;
          margin-top: 10px;
          font-family: arial, sans-serif;
          font-size: 13px;
          color: #222;
        }

        .header-left {
          padding-left: 15px;
          float: left;
        }

        .header-right {
          padding-right: 15px;
          float: right;
        }

        .sign-in-button {
          font-weight: bold;
          border: 1px solid #4285f4;
          border-radius: 2px;
          background-color: #4683ea;
          color: white;
          padding: 0 12px;
          line-height: 28px;
          margin-right: 15px;
          cursor: pointer;
        }

        #main {
          text-align: center;
          padding-top: 90px;
          font-family: arial, sans-serif;
        }

        #search-box-outer {
          display: flex;
          background-color: transparent;
          font: 16px;
          line-height: 34px;
          height: 34px;
          padding: 5px 8px 0 16px;
          margin: 20px auto;
          width: 584px;
          border: none;
          border-radius: 2px;
          box-shadow: 0 3px 8px 1px rgba(0,0,0,0.2), 0 0 0 1px rgba(0,0,0,0.18);
        }

        .search-box-inner {
          border: none;
          background-color: transparent;
          margin: 0;
          padding: 0;
          display: flex;
          flex: 100%;
          height: 33px;
          font-size: 18px;
        }

        .mic {
          width: 24px;
          height: 24px;
          background-size: 24px;
          vertical-align: middle;
          padding: 0px 0px 5px 0px;
          cursor: pointer;
        }

        input:focus {
          outline-width: 0;
        }

        #main-buttons-div {
          display: block;
          padding-top: 6px;
        }

        .search-button {
          align-items: flex-start;
          background-color: #f2f2f2;
          color: #757575;
          font-size: 13px;
          font-weight: bold;
          height: 36px;
          margin: 0px 4px;
          padding: 0px 16px;
          display: inline-block;
          border: solid;
          border-radius: 2px;
          border-width: 1px;
          border-color: #f2f2f2;
        }

        .search-button:hover {
          border-style: solid;
          border-radius: 2px;
          border-width: 1px;
          border-color: rgb(198, 198, 198);
          color: rgb(34, 34, 34);
          background-color: rgb(248, 248, 248);
          cursor: pointer;
        }

        #footer-bar {
          position: absolute;
          display: block;
          bottom: 0;
          left: 0;
          right: 0;
          color: #5f6368;
          background-color: #f2f2f2;
          font-size: 13px;
          font-family: arial, sans-serif;
          line-height: 40px;
          border-top: 1px solid #e4e4e4;
        }

        .footer-left {
          padding-left: 27px;
          float: left;
        }

        .footer-right {
          padding-right: 27px;
          float: right;
        }

        .header-footer-link:hover {
          text-decoration: underline;
          cursor: pointer;
        }
    </style>
</head>
<body>
<h3>
        <header id="header-bar">
            <span class="header-left header-footer-link">About</span>
            <span class="header-left header-footer-link">Store</span>
            <span class="header-right sign-in-button">Sign In</span>
            <span class="header-right header-footer-link">Options</span>
            <span class="header-right header-footer-link">Images</span>
            <span class="header-right header-footer-link">Gmail</span>
        </header>
    
    <div id="main">
            <h1>Dead Internet Reddit</h1>

        <div class="container" id="post-container">
            
        </div>
    </div>
    <footer id="footer-bar">
            <span class="footer-left header-footer-link">Advertising</span>
            <span class="footer-left header-footer-link">Business</span>
            <span class="footer-right header-footer-link">Settings</span>
            <span class="footer-right header-footer-link">Terms</span>
            <span class="footer-right header-footer-link">Privacy</span>
        </footer>
</h3>
</body>
</html>
"""
        return html_content
    
    def get_random_posts(self):
        posts = self.generate_posts(amount=5)
        post_html = ""
        for key, post in posts.items():
            post_html += f"""<div class="post">
                        <h2><a href="{post["link"]}">{post["title"]}</a></h2>
                        <p>{post["text"] if post["text"] else ""}</p>
                        <p>
                            submitted to <a href="{post["link"]}">r/{post["subreddit"]}</a> by <a href="#">u/{post["author"]}</a>, {post["time"]} ago 
                         </p>
                        <p> {post["upvotes"]} Upvotes {post["comments"]} Comments</p>
                         </div>
                        """
        
        html_page = self.home_page.replace('<div class="container" id="post-container">\n            \n        </div>', f'<div class="container" id="post-container">\n            {post_html}        </div>')
        
        return html_page

    def add_comment(self, subreddit_name, post_id, comment_text):
        prompt = f"Generate a Reddit comment with the following text: '{comment_text}'. Return the comment with no other text."
        comment_completion = self.model.generate_content(
              [prompt]
             )
        
        comment = comment_completion.text
        if f"{subreddit_name}/{post_id}" in self.posts:
             self.posts[f"{subreddit_name}/{post_id}"]["comments_list"].append({
                "author": "u/commenter",
                "text": comment,
                "upvotes": random.randint(0, 100),
                "downvotes": random.randint(0, 100),
            })
        
    def get_index(self):
         # Super basic start page, just to get everything going
        return "<!DOCTYPE html><html><body><h3>Enter the Dead Internet</h3><form action='/' ><input name='query'> <input type='submit' value='Search'></form></body></html>"

    def get_page(self, url, path, query=None):
        try: return self.internet_db[url][path]
        except: pass
        
        prompt = f"Give me a classic geocities-style webpage from the fictional site of '{url}' at the resource path of '{path}'. Make sure all links generated either link to an external website, or if they link to another resource on the current website have the current url prepended ({url}) to them. For example if a link on the page has the href of 'help' or '/help', it should be replaced with '{url}/path}}."
        # TODO: I wanna add all other pages to the prompt so the next pages generated resemble them, but since Llama 3 is only 8k context I hesitate to do so

        # Add other pages to the prompt if they exist
        if url in self.internet_db and len(self.internet_db[url]) > 1:
            pass
        
        generated_page_completion = self.model.generate_content([
            self.system_prompt,
            prompt
        ])
        generated_page = generated_page_completion.text
        if not url in self.internet_db:
            self.internet_db[url] = dict()
        self.internet_db[url][path] = generated_page

        open("curpage.html", "w+").write(generated_page)
        return generated_page
    
    def get_search(self, query):
        prompt = f"Generate the search results page for a ficticious search engine where the search query is '{query}'. Please include at least 10 results to different ficticious websites that relate to the query. DO NOT link to any real websites, every link should lead to a ficticious website. Feel free to add a bit of CSS to make the page look nice. Each search result will link to its own unique website that has nothing to do with the search engine. Make sure each ficticious website has a unique and somewhat creative URL. Don't mention that the results are ficticious."
        search_page_completion = self.model.generate_content([
            self.system_prompt,
            prompt
        ])
        return search_page_completion.text
    
    def get_subreddit(self, subreddit_name):
        prompt = f"Generate the page for a subreddit called '{subreddit_name}'. Make sure to add a few fake posts to the subreddit page, make sure that each post on the page has a link to it as well. Don't mention anything about this page being generated by an AI. Add a description of the subreddit, number of subscribers, and rules. Add the ability to add a post to the subreddit. make sure the link to each post uses the /r/subreddit/post-id format."
        subreddit_page_completion = self.model.generate_content([
            self.system_prompt,
            prompt
        ])
        return subreddit_page_completion.text

    def get_post(self, subreddit_name, post_id):
        post_key = f"{subreddit_name}/{post_id}"
        post_data = self.posts.get(post_key, None)
        if not post_data:
            return "Post not found"
            
        comment_html = ""
        for comment in post_data["comments_list"]:
             comment_html += f"""<div class="comment">
                            <p> {comment["text"]} </p>
                            <p> by {comment["author"]} </p>
                            <p> {comment["upvotes"]} upvotes, {comment["downvotes"]} downvotes</p>
                            </div>
                         """
        
        post_page_completion = self.model.generate_content([
            self.system_prompt,
            f"Generate the page for the post with the id of '{post_id}' in the subreddit of '{subreddit_name}'. Make sure to add a title and the body of the post. Don't mention anything about this page being generated by an AI. make sure to add links to the subreddit using the /r/subreddit url. Don't generate a reply box."
        ])
        
        post_html = post_page_completion.text
        post_html = f"""
                    {post_html}
                    <h2> Comments </h2>
                    {comment_html}
                     <form method="post">
                    <textarea name="comment" placeholder="Add a comment"></textarea>
                    <input type="submit" value="Post Comment">
                     </form>
                     """
        
        return post_html


    def export_internet(self, filename="internet.json"):
        json.dump(self.internet_db, open(filename, "w+"))
        russells  = "Russell: I'm reading it here on my computer. I downloaded the internet before the war.\n"
        russells += "Alyx: You downloaded the entire internet.\n"
        russells += "Russell: Ehh, most of it.\n"
        russells += "Alyx: Nice.\n"
        russells += "Russell: Yeah, yeah it is."
        return russells