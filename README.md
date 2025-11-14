# 30 Days of Coding

This repository contains daily coding projects, each designed to teach and reinforce programming concepts, data processing, and automation skills. Every day features a self-contained project with its own explanation and code.

## Structure

- Each day has its own folder (e.g., `day-1-2025-nov-13/`).
- Each folder contains:
  - Source code
  - Sample data (if applicable)
  - A README explaining the day's project

## How to Use

1. Browse to any day's folder.
2. Read the day's README for an overview and instructions.
3. Run the code as described.

## Requirements

- Python 3.x
- Additional dependencies listed in each day's README

---

# Day 1: Data Cleaner ETL Pipeline

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python, pandas, and SQLite.

## What It Does

- **Extract:** Reads raw order data from `orders_raw.csv`.
- **Transform:** 
  - Standardizes customer names to title case.
  - Fills missing `amount` values with the average.
  - Filters for completed orders only.
- **Load:** Saves cleaned data to a local SQLite database (`orders.db`) in the `clean_orders` table.
- **Summary:** Prints ETL statistics, including total revenue and top customer.

## How to Run

1. Install dependencies:
   ```sh
   pip install pandas
   ```
2. Run the script:
   ```sh
   python data_cleaner.py
   ```

## Output

- Prints summary statistics to the console.
- Creates/updates `orders.db` with cleaned data.

---

# Day 2: Random User ETL Pipeline

This project fetches random user data from an API, processes it, and loads it into a local SQLite database.

## What It Does

- **Extract:** Fetches 10 random users from the [randomuser.me](https://randomuser.me/) API.
- **Transform:** Flattens the JSON data and selects relevant fields (first name, last name, gender, email, city, country).
- **Load:** Saves the user data to a local SQLite database (`users.db`) in the `random_users` table.
- **Summary:** Prints the number of users fetched, counts by gender, and the top 3 countries represented.

## How to Run

1. Install dependencies:
   ```sh
   pip install pandas requests
   ```
2. Run the script:
   ```sh
   python etl_users.py
   ```

## Output

- Prints summary statistics to the console.
- Creates/updates `users.db` with user data.

---
