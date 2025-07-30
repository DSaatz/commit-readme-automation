
# Commit README Automation

A lightweight GitHub Action to automatically update your profile README with your **most recent commits**.  
Inspired by [br0sinski/readmefetch](https://github.com/br0sinski/readmefetch), but designed to be **minimal** and easily integrated with existing profile README setups.

The output is formatted to be reminiscent of a **terminal window**, giving your profile a clean, console-like look.

---

## 🔧 Setup

### 1️⃣ Clone and Upload
- Clone this repository.
- Upload it to your own GitHub account as a new repo.

### 2️⃣ Create a Personal Access Token
- Go to: **Settings > Developer Settings > Personal Access Tokens > Tokens (classic)**.
- Generate a token with **repo** scope (read/write).

### 3️⃣ Add Repository Secrets
In your new repo, go to **Settings > Secrets and variables > Actions** and add:

- `GH_USERNAME` → Your GitHub username (exactly as your profile).
- `GH_TOKEN` → The token you generated.

### 4️⃣ Add Activity Markers to Your Profile README
In your profile repo (`<username>/<username>`), edit `README.md` and insert:

```markdown
<!--RECENT_ACTIVITY_START-->
<!--RECENT_ACTIVITY_END-->
```

You can see an example of how this looks on [my profile](https://github.com/DSaatz).

### 5️⃣ Trigger the Action
- The workflow runs every 30 minutes automatically.
- You can also trigger it manually under **Actions > Update Profile README from External Repo**.

---

## 📜 Environment Variables

| Name         | Value                                                   |
|--------------|---------------------------------------------------------|
| `GH_USERNAME` | Your GitHub username                                    |
| `GH_TOKEN`    | Personal access token with repo read/write permissions  |

---

## ✅ Notes

- The script clones your profile repo (`<username>/<username>`), injects the latest commits into your README between the markers.
- The output is styled as an ASCII terminal block for a clean, retro look.

# Commit README Automation

A lightweight GitHub Action to automatically update your profile README with your **most recent commits**.  
Inspired by [br0sinski/readmefetch](https://github.com/br0sinski/readmefetch), but designed to be **minimal** and easily integrated with existing profile README setups.

The output is formatted to be reminiscent of a **terminal window**, giving your profile a clean, console-like look.

---

## 🔧 Setup

### 1️⃣ Clone and Upload
- Clone this repository.
- Upload it to your own GitHub account as a new repo.

### 2️⃣ Create a Personal Access Token
- Go to: **Settings > Developer Settings > Personal Access Tokens > Tokens (classic)**.
- Generate a token with **repo** scope (read/write).

### 3️⃣ Add Repository Secrets
In your new repo, go to **Settings > Secrets and variables > Actions** and add:

- `GH_USERNAME` → Your GitHub username (exactly as your profile).
- `GH_TOKEN` → The token you generated.

### 4️⃣ Add Activity Markers to Your Profile README
In your profile repo (`<username>/<username>`), edit `README.md` and insert:

```markdown
<!--RECENT_ACTIVITY_START-->
<!--RECENT_ACTIVITY_END-->
```

This will be the space in which your "console" will be displayed.

You can see an example of how this looks on [my profile](https://github.com/DSaatz).

### 5️⃣ Trigger the Action
- The workflow runs every 30 minutes automatically. 
- You may change the value in the yml if you like it to trigger more often which I personally think would be redundant.
- You can also trigger it manually under **Actions > Update Profile README from External Repo**.

---

## 📜 Environment Variables

| Name         | Value                                                   |
|--------------|---------------------------------------------------------|
| `GH_USERNAME` | Your GitHub username                                    |
| `GH_TOKEN`    | Personal access token with repo read/write permissions  |

---

## ✅ TL:DR
- Env Vars ➡️ look into table above.
- The script clones your profile repo (`<username>/<username>`), injects the latest commits into your README between the markers.
- The output is styled as an ASCII terminal block for a clean, retro look.
