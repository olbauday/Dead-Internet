def get_index():
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
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
        <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google logo">
        <br>
        <form action="">
            <div id="search-box-outer">
                <input class="search-box-inner" input name='query'>
                <span><img class="mic" src="https://www.gstatic.com/images/branding/googlemic/2x/googlemic_color_24dp.png" alt="voice command button"</span>
            </div>
            <br>
            <div id="main-buttons-div">
                <input type="submit" class="search-button" value="Search">
                <input type="submit" class="search-button" value="I'm Feeling Lucky">
            </div>
        </form>
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