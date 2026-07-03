# Knowledge Notes: HTTP, APIs, And External Data

## Core Ideas

APIs let your program fetch data from another system. The response may be slow, missing, malformed, rate-limited, or unavailable.

Keep API work in layers:

- fetch raw data
- parse or normalize it
- summarize it
- display or save it

## HTTP Basics

Important status code groups:

- `2xx`: success
- `3xx`: redirect
- `4xx`: client error, such as not found or unauthorized
- `5xx`: server error

Always handle non-success responses.

## JSON Responses

Most web APIs return JSON.

```python
data = response.json()
```

After parsing JSON, validate the shape you need. Public APIs can change or omit fields.

## Timeouts And Retries

Network calls should have timeouts. Without a timeout, a program can hang.

Retry only failures that might be temporary, such as timeouts or `5xx` responses. Do not blindly retry invalid input.

## Caching

Caching saves a response for reuse.

Useful cache metadata:

- when the data was fetched
- what URL or username it belongs to
- the raw response payload

Use caching to avoid rate limits and speed up repeated development.

## Testing API Code

Avoid live network calls in unit tests. Use saved sample responses.

Good functions to test:

- response parsing
- normalization
- summary generation
- cache freshness checks

## Boundaries

Keep API-specific details near the fetching/parsing layer. The rest of the program should work with your own clean data shape.

## Common Mistakes

- Assuming every response is successful.
- Assuming every JSON field exists.
- Mixing fetch logic and output formatting.
- Letting tests depend on a live API and internet connection.

