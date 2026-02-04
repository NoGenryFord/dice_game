# Як зробити гілку main default / How to Set Main as Default Branch

## Локальна конфігурація Git / Local Git Configuration

Щоб встановити `main` як назву гілки за замовчуванням для нових репозиторіїв:

To set `main` as the default branch name for new repositories:

```bash
git config --global init.defaultBranch main
```

## Встановлення гілки за замовчуванням на GitHub / Setting Default Branch on GitHub

Щоб встановити гілку `main` як гілку за замовчуванням для репозиторію на GitHub:

To set the `main` branch as the default branch for a repository on GitHub:

### Через веб-інтерфейс GitHub / Via GitHub Web Interface

1. Перейдіть до вашого репозиторію на GitHub / Navigate to your repository on GitHub
2. Натисніть на **Settings** (Налаштування) / Click on **Settings**
3. У лівому меню виберіть **Branches** / In the left menu, select **Branches**
4. У розділі **Default branch** натисніть кнопку з іконкою переключення / In the **Default branch** section, click the switch icon
5. Виберіть `main` зі списку гілок / Select `main` from the list of branches
6. Натисніть **Update** (Оновити) / Click **Update**
7. Підтвердіть зміни, натиснувши **I understand, update the default branch** / Confirm by clicking **I understand, update the default branch**

### Через GitHub CLI / Via GitHub CLI

```bash
gh repo edit --default-branch main
```

### Через GitHub API / Via GitHub API

```bash
curl -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  https://api.github.com/repos/OWNER/REPO \
  -d '{"default_branch":"main"}'
```

## Примітки / Notes

- Переконайтеся, що гілка `main` існує перед тим, як встановити її за замовчуванням
- Make sure the `main` branch exists before setting it as default

- Після зміни гілки за замовчуванням, нові Pull Request будуть автоматично створюватися для гілки `main`
- After changing the default branch, new Pull Requests will automatically target the `main` branch

- Локальні клони репозиторію потрібно буде оновити, щоб відстежувати нову гілку за замовчуванням
- Local clones of the repository will need to be updated to track the new default branch
