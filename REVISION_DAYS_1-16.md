# Python Revision — Days 1–16

A consolidation of everything from Phase 1 so far, written for a senior Java
engineer. Every concept is anchored to its Java equivalent. Read it once to
refresh; then use the **Re-test yourself** section at the end to check what
actually stuck.

---

## 1. The execution model (Day 1)

- A Python file runs **top to bottom**. There is no separate compile pass that
  reads the whole file first.
- `def` and `class` are **statements that execute** — they *bind a name* to a
  function/class object at the moment the line runs. They are not declarations
  the compiler pre-registers.
- Consequence: you cannot call a function before the `def` line has run —
  `NameError`. Java hoists method declarations; Python does not.
- **Indentation IS the block structure.** No braces. Your eyes and the
  interpreter read the same thing. A whitespace mistake is a *semantic* error,
  not a style complaint.

```python
print("A")
def greet():
    print("B")
print("C")
greet()
# Output: A, C, B  — greet() body runs only when called
```

---

## 2. Variables and typing (Day 3)

- A variable is a **name tag**, not a typed box. `x = 5` sticks the label `x`
  on an int object. `x = "hi"` peels it off and sticks it on a string. The label
  has no type; the *object* carries the type.
- **Dynamic** = types checked at *runtime*, not compile time.
- **Strong** = Python does NOT auto-convert. `5 + "hi"` is a `TypeError`, not
  `"5hi"`. This is *stricter* than Java, which silently makes `"5hi"`.
- Conversion is explicit and means the human-facing operation:
  - `int("42")` → parse text as a number (`int("hello")` → `ValueError`)
  - `str(42)` → write number as text
  - `int(3.5)` → truncate a float → `3`   (but `int("3.5")` → `ValueError`)
  - `float("3.5")` → `3.5`
- `None` is Python's `null`. The word is `None`, capital N. `null` does not exist.

Error names to recognize:
- `TypeError` — wrong *kind* of thing (int + str)
- `ValueError` — right kind, bad *content* (`int("hello")`)

---

## 3. The four containers (Days 4–6)

| Python | Java | Literal | Notes |
|--------|------|---------|-------|
| `list` | `ArrayList` | `[1, 2, 3]` | ordered, mutable, indexed, untyped elements |
| `dict` | `HashMap` | `{"a": 1}` | key → value |
| `set`  | `HashSet` | `{1, 2, 3}` | unique, unordered |
| `tuple`| *(none)* | `(1, 2, 3)` | **immutable** sequence |

### list (Day 4)
- Zero-based indexing like Java: `nums[0]`.
- **Negative indices** count from the end: `nums[-1]` last, `nums[-2]` second-last.
- **Slicing** `nums[start:end]` → a *new list*, end **exclusive**.
  - `nums[:3]` from start; `nums[2:]` to end; `nums[:0]` is empty `[]`.
  - Element count = `end - start`.
- `.append(x)` grows the list (= `ArrayList.add`).

### dict (Day 5)
- Lookup with brackets: `ages["Ameya"]`.
- **Missing key → `KeyError`** (loud), unlike Java's silent `null`.
- `.get(key)` → `None` if absent; `.get(key, default)` → your fallback. This is
  where you opt into Java-style "return something instead of crashing."
- Write: `d["new"] = value`.

### set (Day 5)
- Duplicates collapse automatically. No positional access — `s[0]` is a
  `TypeError` (a set has no order). Use `in` for membership, or `list(s)` if you
  genuinely need positions (a sign you wanted a list).
- **`{}` is an empty *dict*, not a set.** Empty set is `set()`.

### tuple (Day 6)
- Like a list but cannot be changed after creation. Slicing a tuple returns a tuple.
- Three uses: **multiple return values**, **dict keys** (must be immutable),
  signalling a fixed group.
- Packing/unpacking:
  ```python
  def stats(nums):
      return min(nums), max(nums)   # packs a tuple
  low, high = stats([3, 1, 8])      # unpacks into two names
  ```

### Container choice rule
- Need **position/order** → `list`
- Need fast **"is it in here?"** + dedup → `set`
- Need **key → value** → `dict`
- If the operation you want doesn't exist on the container, you picked the wrong one.

---

## 4. Numbers gotcha (Day 6)

- `/` is **always** float division: `17 / 5 == 3.4`. (Java gives `3` for int/int.)
- `//` is floor division: `17 // 5 == 3`.
- `%` is remainder: `17 % 5 == 2`.
- `**` is exponentiation: `2 ** 10 == 1024`. (No `Math.pow`.)

---

## 5. Control flow (Day 7)

- `if` / `elif` / `else` — no parens around the condition, colon + indent.
  `elif` is one word.
- Logic operators are **words**: `and`, `or`, `not` (not `&&`, `||`, `!`).
- **`for` is for-each ONLY.** There is no C-style `for(i=0; i<n; i++)` in Python.
  You iterate elements, not indices.
  ```python
  for item in mylist: ...
  ```
- Need the index? `enumerate`:
  ```python
  for i, item in enumerate(mylist): ...   # i is the position
  ```
- Need to loop N times / a number range? `range`:
  - `range(5)` → 0,1,2,3,4 (end-exclusive, like slicing)
  - `range(2, 5)` → 2,3,4
  - `range(0, 10, 2)` → 0,2,4,6,8 (start, stop, step)
- `while condition:` — identical to Java.
- `print` behaves like Java's `println` — newline after every call. Line breaks in
  output depend on **how many times print runs**, not how many args you pass it.
  `print(a, b)` → one line, space-separated.

---

## 6. Functions (Day 8)

```python
def add(a, b):
    return a + b
```

- No return type, no parameter types. Colon + indented body.
- **No `void`.** A function with no `return` returns `None` (silently — a
  forgotten return means `None` flows downstream until it breaks).
- **Default arguments** replace Java method overloading:
  ```python
  def greet(name, greeting="Hello"):
      return f"{greeting}, {name}"
  ```
- Multiple return = pack a tuple, unpack at the call site.

---

## 7. Comprehensions (Days 9–10)

The map/filter/collect pipeline folded into bracket syntax. It's an **expression
that evaluates to a whole container** — one value, not a loop.

```python
[n * 2 for n in nums]                 # list — like .map()
[n for n in nums if n % 2 == 0]       # list — .filter()
[n * n for n in nums if n % 2 == 0]   # filter THEN transform
{n: n * n for n in nums}              # dict comprehension  {k: v ...}
{n * n for n in nums}                 # set comprehension   {v ...}
```

- Written transform-first; **runs** source → filter → transform.
- The bracket picks the container: `[]` list, `{k:v}` dict, `{v}` set.
- Judgment: use one when it's *clearer*, not just shorter. A tangled comprehension
  is worse than a plain loop.

---

## 8. f-strings (Day 10)

```python
f"Day {day}: {name} earned {xp} XP"
```

- `f` prefix; `{expr}` evaluates any expression and inserts it.
- Auto-converts types — no `str()` needed inside the braces.
- Everything *outside* `{}` is literal text — quotes, parens, commas print as-is.
- Formatting: `{price:.2f}` (2 decimals), `{ratio:.1%}` (percentage).

---

## 9. Classes and OOP (Days 11–13)

```python
class BankAccount:
    def __init__(self, balance):     # constructor
        self.balance = balance        # field springs into existence on assignment

    def deposit(self, amount):        # every method's 1st param is self
        self.balance += amount
```

- `class Name:` — colon + indent, no braces.
- `__init__` is the constructor (fixed name, not the class name).
- **`self` is an explicit `this`.** Always the first parameter of every method;
  **never passed manually** — `acc.deposit(50)` not `acc.deposit(acc, 50)`.
- Fields are created by assigning `self.x = ...`; no separate declaration.
- **No `new`** — construct with `BankAccount(100)`.
- `self` appears ONLY inside class methods. A free-standing function has no `self`.
- Methods must **read `self.field`**, not hardcode literals — that's what makes one
  method work for any instance (polymorphism).

### Inheritance (Day 12)
```python
class Manager(Employee):              # (Parent) = extends
    def __init__(self, name, salary, team):
        super().__init__(name, salary)  # = Java super(...); note the ()
        self.team = team

    def describe(self):               # override — automatic, no @Override
        ...
```
- Child inherits the parent's `__init__` if it defines none.
- `super().__init__(...)` — note the **parentheses** on `super()`.

### Dunder methods (Day 13)
Python calls specially-named methods when things happen to your object:
- `__init__` — construction
- `__str__` — `toString()`. Must **RETURN** a string, never print. Called by
  `print(obj)`, `str(obj)`, f-strings.
- `__eq__(self, other)` — `equals()`, wired to the `==` operator. Default `==`
  compares **identity** (same object?) like Java; override to compare *contents*.
- Dunders = **operator overloading**, which Java lacks (`__add__` → `+`, etc.).

---

## 10. Exceptions (Day 14)

```python
try:
    x = int("hello")
except ValueError as e:
    print(f"Failed: {e}")
finally:
    print("always runs")
```

- `try:` / `except ErrorType:` = try/catch. `except` catches the type you name
  and lets other types propagate.
- `as e` binds the error object (= Java's `catch (ValueError e)`).
- `finally` always runs — cleanup regardless of outcome.
- `raise ValueError("msg")` = `throw`.
- **Key distinction:** `raise` = *you produce* an error signal. `except` = *you
  react* to one. Don't raise the thing you were asked to catch.
- An exception aborts the current block immediately and jumps to the handler —
  lines after the failure don't run.

---

## 11. Modules (Day 15)

- Every `.py` file is a **module**, named by its filename. (A module is a *file* —
  not a class. A module can hold many classes/functions or none.)
- Import forms:
  ```python
  import mathutils                  # use mathutils.add
  from mathutils import add         # use add directly
  from mathutils import add, PI     # several; can import functions AND variables
  ```
- No class requirement — you import whatever is at the file's top level.
- `__name__` is `"__main__"` when the file is **run directly**, and the module
  name when it's **imported**.
  ```python
  if __name__ == "__main__":
      # run-directly code (tests/demo) — skipped on import
  ```
  Note both sides: `__name__` is a variable (no quotes); `"__main__"` is a string.
- Scope catch: a function's parameters don't exist outside the function.

---

## 12. File I/O (Day 16)

```python
# write
with open("data.txt", "w") as f:
    f.write("apple\n")            # write does NOT add \n — you add it

# read, line by line (idiomatic, memory-efficient)
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())      # strip the trailing \n
```

- `open(path, mode)` — modes: `"w"` overwrite (creates/truncates), `"r"` read
  (default), `"a"` append.
- `with open(...) as f:` = **try-with-resources** — guaranteed close, even on
  exception. No `f.close()` needed. (The mechanism is a *context manager* =
  `AutoCloseable`.)
- `f.read()` → whole file as one string. `f.readlines()` → list of lines.
- `\n` is **one** character (a newline), not two. In source you type `\n`; in the
  file it becomes an actual line break.
- **Lines read from a file carry their trailing `\n`** — `.strip()` before printing
  (avoids double-spacing) or comparing (`"apple\n" != "apple"` → silent bug).

---

## Re-test yourself (do these on the laptop before Day 17)

Don't just re-read — *write these cold* and run them. If any feel shaky, that's the
one to redo. These target the things most likely to have faded over the break.

1. **Trace, don't run:** what does this print, in what order?
   ```python
   print("A")
   def f(): print("B")
   print("C")
   f()
   ```

2. **Predict:** `print(17 / 5, 17 // 5, 17 % 5)`

3. **Predict the shape:** does this crash, print, or return something?
   ```python
   d = {"a": 1}
   print(d["z"])
   print(d.get("z", 0))
   ```

4. **Write cold:** a list comprehension that takes `[1,2,3,4,5,6]` and produces the
   squares of only the even numbers. (Expected `[4, 16, 36]`.)

5. **Write cold:** a class `Point` with `__init__(self, x, y)`, a `__str__` that
   prints `Point(3, 5)`, and an `__eq__` so two Points with the same coords are equal.

6. **Write cold:** a function `safe_int(s)` that returns `int(s)`, but returns `-1`
   if `s` can't be parsed (catch the `ValueError`).

7. **Write cold:** write three names to a file, then read them back and print each
   with no double-spacing.

Answers are all in the sections above. If you get 5, 6, and 7 cleanly from a blank
file, you're ready for the Day 17 consolidation exercise and on track for the
Phase 1 boss (~Day 30).

---

## Where you are

- **Phase 1 (Days 1–30): Python via Java** — you're at Day 16, just past halfway.
- **Rank:** Syntax Initiate. **XP:** 3350.
- **Next:** Day 17 — a multi-concept consolidation (classes + file I/O + exceptions
  in one small program), the warm-up for the boss battle's shape.
- **Boss battle (~Day 30):** build a small CLI tool from scratch, tested and
  committed — no scaffolding. That's the gate to rank up to **Pythonista** and
  enter Phase 2 (NumPy, pandas, the math).
