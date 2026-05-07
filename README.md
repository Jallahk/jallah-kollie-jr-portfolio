<<<<<<< HEAD
# Jallah Kollie Jr Portfolio

This portfolio is ready to be published with GitHub Pages so you can use a public `https://...` link on your resume instead of a local `file:///...` path.

## Why the old resume link did not work

The old link pointed to a file on your personal computer:

```text
file:///Users/jallahkollie/PycharmProjects/PythonMiniProject%20/Machine%20Learning/Jallah-Kollie-Jr-Portfolio/index.html
```

That path only exists on your machine. Recruiters and employers cannot open files that live on your laptop, and many PDF viewers block local file links for security reasons.

## Best fix

Publish this folder to GitHub Pages and use the public URL on your resume.

Your future resume link will look like one of these:

- `https://YOUR_GITHUB_USERNAME.github.io/jallah-kollie-jr-portfolio/`
- `https://YOUR_GITHUB_USERNAME.github.io/`

The second option works if you name the repository exactly `YOUR_GITHUB_USERNAME.github.io`.

## Fastest GitHub Pages setup

### Option 1: Regular repository

1. Create a new GitHub repository named `jallah-kollie-jr-portfolio`
2. Open Terminal in this folder
3. Run:

```bash
cd "/Users/jallahkollie/PycharmProjects/PythonMiniProject /Machine Learning/Jallah-Kollie-Jr-Portfolio"
git init
git add .
git commit -m "Initial portfolio site"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/jallah-kollie-jr-portfolio.git
git push -u origin main
```

4. On GitHub, open the repository
5. Go to `Settings` -> `Pages`
6. Under `Build and deployment`, choose:
   - `Source`: `Deploy from a branch`
   - `Branch`: `main`
   - `Folder`: `/ (root)`
7. Save

Your live URL will be:

```text
https://YOUR_GITHUB_USERNAME.github.io/jallah-kollie-jr-portfolio/
```

### Option 2: Personal site repository

If you want a cleaner resume link, create a repository named:

```text
YOUR_GITHUB_USERNAME.github.io
```

Then push this portfolio into that repository instead. Your live URL will be:

```text
https://YOUR_GITHUB_USERNAME.github.io/
```

## After publishing

Replace the `file:///...` link on your resume with your GitHub Pages link.

Example:

```text
https://YOUR_GITHUB_USERNAME.github.io/jallah-kollie-jr-portfolio/
```

Then re-export your resume PDF.

## Updating the portfolio later

If you make changes later, regenerate the site data if needed:

```bash
python3 generate_portfolio.py
```

Then commit and push:

```bash
git add .
git commit -m "Update portfolio"
git push
```

## Files included for GitHub Pages

- `index.html`
- `style.css`
- `script.js`
- `data/projects.js`
- `.nojekyll`

The `.nojekyll` file helps GitHub Pages serve the site exactly as a static folder.
=======
# jallah-kollie-jr-portfolio
>>>>>>> 6259bf1b64e8e357aa579f822dfac20923571e13
