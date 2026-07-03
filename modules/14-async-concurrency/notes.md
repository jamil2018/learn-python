# Knowledge Notes: Async And Concurrency Basics

## Core Ideas

Concurrency lets multiple tasks make progress during waiting time. It is most useful for I/O-bound work such as network requests and file waits.

It does not automatically make CPU-heavy calculations faster.

## Async Functions

```python
import asyncio

async def fetch_fake():
    await asyncio.sleep(1)
    return "done"
```

Call async code from an event loop:

```python
result = asyncio.run(fetch_fake())
```

## Running Tasks Together

```python
results = await asyncio.gather(task_one(), task_two(), task_three())
```

`gather()` runs awaitables concurrently and returns results in order.

## Timeouts

```python
result = await asyncio.wait_for(fetch_fake(), timeout=2)
```

Timeouts prevent one slow operation from hanging the whole program forever.

## Handling Errors

Concurrent code still needs clear error handling. Consider returning structured results:

```python
{
    "url": url,
    "ok": False,
    "error": "timeout",
}
```

This is often better than crashing the entire batch.

## Limiting Concurrency

Too much concurrency can overload your machine or a remote service.

```python
semaphore = asyncio.Semaphore(5)

async with semaphore:
    return await check_url(url)
```

## TypeScript Lens

Python `async`/`await` feels similar to TypeScript, but the event loop is explicit with `asyncio.run()`. Python has no built-in `Promise.all`; `asyncio.gather()` is the closest common tool.

## Common Mistakes

- Forgetting to `await` an async function.
- Using async for CPU-heavy work and expecting speedups.
- Launching unlimited tasks.
- Letting one failed task destroy an entire batch when partial results would be better.

