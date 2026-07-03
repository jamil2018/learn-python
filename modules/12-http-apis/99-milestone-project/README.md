# Milestone Project: GitHub Profile Summarizer

Build a command-line tool that fetches public GitHub profile data and summarizes it.

## Required Features

- Accept a GitHub username.
- Fetch public profile data.
- Fetch public repositories.
- Show repository count, follower count, and most-used repository languages where available.
- Save a JSON snapshot.
- Generate a readable text summary.

## Stretch Goals

- Add caching to avoid repeated API calls.
- Export CSV.
- Handle rate limit responses gracefully.

## Completion Criteria

- Network failures do not crash with an unreadable traceback.
- API parsing is separated from summary generation.
- Tests use saved sample responses instead of live network calls.

