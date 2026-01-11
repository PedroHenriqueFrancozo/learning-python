# Set Operators - Master Guide 🧮

This lesson covers the four main mathematical operations that can be performed on Python Sets. These are essential for high-performance data comparison.

### :clipboard: Summary of Operators:

1.  **Union (`|`):** Merges sets. Great for combining lists of IDs or emails without duplicates.
2.  **Intersection (`&`):** Finds common ground. Use this to see which users belong to two different groups at the same time.
3.  **Difference (`-`):** "Subtraction". Use it to filter out "blocked" items from a main list.
4.  **Symmetric Difference (`^`):** Finds the outliers. Returns everything except what the sets have in common.

---

### 🛠️ Visual Table:

| Operator | Math Name | Result Example |
| :--- | :--- | :--- |
| `\|` | Union | All elements combined |
| `&` | Intersection | Only shared elements |
| `-` | Difference | Elements exclusive to the first set |
| `^` | Symm. Difference | Elements not shared by both |

---

### 💡 Pro Tip:
Set operations are much faster than using `for` loops and `if` statements to compare lists. When performance matters, always convert your data to a `set` first!