# Milestone Project: Weekend Trip Planner

Build a terminal program that helps someone plan a short trip. The program runs top to bottom in one session: greet the user, collect a few numbers, do the math, and print clearly formatted results.

## Required Features

1. **Greeting**
   - Ask for the user's name and print a short welcome message.

2. **Travel time**
   - Ask for distance (km) and average speed (km/h).
   - Estimate travel time as whole hours and remaining minutes.

3. **Download time**
   - Ask for a file size in MB and download speed in Mbps.
   - Estimate download time as whole minutes and remaining seconds.

4. **Dinner receipt**
   - Ask for a bill amount and tip percentage.
   - Print a small receipt with aligned labels and dollar amounts for:
     - Subtotal
     - Tip
     - Total

5. **Trip summary**
   - Print a short summary block that repeats the key results from the sections above.

## Constraints

- Use only concepts from Module 1: variables, `input()`, `print()`, math operators, type conversion, f-strings, and `round()`.
- Keep everything in one Python file.
- Do not use loops, conditionals, functions, lists, or dictionaries.
- Invalid numeric input may crash; you will learn better validation later.

## Completion Criteria

- The program runs from start to finish without restarting.
- Each section asks for input and prints a readable result.
- Time breakdowns use `//` and `%` (not only floating-point division).
- Money values are formatted with two decimal places (for example, `$12.50`).
- You manually test the program with at least 2 different input sets and confirm the output looks reasonable.

## Example Flow

```
Name: Ada
Distance (km): 150
Speed (km/h): 60
File size (MB): 800
Download speed (Mbps): 50
Bill amount: 42.50
Tip (%): 18

Hello, Ada!

Travel time: 2 hour(s) 30 minute(s)
Download time: 2 minute(s) 40.00 second(s)

Subtotal     $42.50
Tip          $7.65
Total        $50.15

--- Trip Summary ---
Travel: 2 hour(s) 30 minute(s)
Download: 2 minute(s) 40.00 second(s)
Dinner total: $50.15
```
