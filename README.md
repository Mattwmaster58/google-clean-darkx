# Google - Clean Dark Extended
[![PRs Accepted](https://img.shields.io/badge/pull%20requests-accepted-green)](https://github.com/Mattwmaster58/google-clean-darkx/pulls)


📦 [Install the usercss](https://raw.githubusercontent.com/Mattwmaster58/google-clean-darkx/master/google-clean-darkx.min.user.css). It supports automatic updates.

This theme is a continuation of [this](https://userstyles.org/styles/144028/google-clean-dark)
(by [Seishiin](https://userstyles.org/users/352024)) userstyle (which hasn't seen any update for over a year now) with improvments made by me as needed.

## Screenshots

Coming soon™

## Contributing

### Recommended Workflow

The Stylus extension doesn't deal nicely with 200kb styles, so we need to work around that. Here's what I've found works
nicely:
- Start a HTTP server with `python -m http.server` in the root of the project dir
- Make any changes in your browser's dev tools
- Modify the appropriate file(s)
- Run `./build.py`
- Install the UserStyle from http://localhost:8000/google-clean-darkx.min.user.css
- Observe that it works (hopefully)

### Contributing Guidelines

This repo is always accepting pull requests and it will go a lot smoother if you follow these guidelines:
 - Modify the relevant file:
   - Don't modify [google-clean-darkx.min.user.css](/google-clean-darkx.min.user.css), that's the built file. Instead, modify the appropriate file in [./css](/css)
 - Don't change the version, the CI will do that automatically
 - Please include a short description of the results of the change, as well as a before/after screenshot

## Future Potential Improvements/TODO
###### When I have the time + feel like it
In order of descending importance.
 - Use CSS Color variables
 - Merge in better looking google search styles
 - Deploy to [userstyles.org](https://userstyles.org)

