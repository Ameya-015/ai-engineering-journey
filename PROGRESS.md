# AI Engineering Journey — 180 Days

Java backend engineer → AI engineer.

---
## Day 39 — 2026-11-09 · 250 XP
**Learned:** dtypes: int64, float64, bool, str, datetime64. Numbers stored as
TEXT give silent wrong answers (sort '10' < '9', max '9', + concatenates).
`.astype(int/float/str)` converts → new Series; raises on bad values; float →
int truncates. NaN can't be `int64` → use `"Int64"` (capital I = nullable,
like Java `Integer` vs `int`; missing shows as `<NA>`).
`pd.to_numeric(col, errors="coerce")` turns junk ("unknown") into NaN.
`read_csv(..., dtype={"id": str})` stops IDs losing leading zeros (007 → 7).
Booleans from text: `df["paid"] = df["paid"] == "yes"`. read_csv already
treats "n/a" as missing. Sums over gaps undercount (680 = complete orders only).

## Day 38 — 2026-11-08 · 250 XP
**Learned:** Missing values. `NaN == NaN` is False, so `== np.nan` never
finds anything — use `.isna()` / `.notna()`. `df.isna().sum()` = missing per
column; `df[df.isna().any(axis=1)]` = rows with any gap. `.count()` counts
PRESENT values (present + missing = len). Aggregations skip NaN.
`dropna()` (optionally `subset=[...]`) removes rows; `fillna(value)` or
`fillna({"col": value})` replaces gaps. Both return NEW objects. The choice
changes results: on my reading log, filling with means raised mean
pages/min from 0.745 to 0.855, because the invented rows gave the two
highest speeds. Fill with a flag column to keep the trace.
**Reflection:** Compared two different metrics (pages vs pages/min) and
divided one table's column by another's. 

## Day 37 — 2026-11-06 · 250 XP
**Learned:** `pd.read_csv(path)` → DataFrame (header row = column names,
types inferred). Paths are relative to the notebook's folder; data lives in
`data/`. Dates stay TEXT unless `parse_dates=["date"]`. Missing cells → `NaN`
("Not a Number", a float). First look at any new data: `.head()`, `.shape`,
`.info()` (non-null counts reveal gaps), `.describe()` (stats for numeric and
date columns, skips text). NaN propagates through math (`75 / NaN` → NaN),
and one NaN turns an int column into float64.


## Day 36 — 2026-11-06 · 250 XP
**Learned:** Jupyter notebooks (`.ipynb`) in VS Code — Jupyter extension +
`ipykernel` in the venv; Select Kernel → `.venv`. A notebook = cells run one
at a time (Shift+Enter); variables persist in the kernel's memory between
cells (like jshell, saved as a document). The last expression in a cell
displays itself; DataFrames render as tables. Code cells vs Markdown cells
(notes, findings). The trap: RUN ORDER is what counts — re-running a cell
changes state invisibly (`[n]` shows run order). Rule: Restart → Run All
before sharing or committing; numbers must run [1], [2], [3] in order.
**Reflection:** Markdown notes should record findings about the data, not about the tool.

## Day 35 — 2026-11-03 · 250 XP
**Learned:** `*args` collects extra positional args into a TUPLE (= Java
varargs `int... nums`; empty call → `()`, never null). `**kwargs` collects
extra keyword args into a DICT (no Java equivalent). Named parameters claim
their arguments first; `*args`/`**kwargs` get only the leftovers, and a
claimed argument appears in exactly one place. Order: normal, `*args`,
keyword-only, `**kwargs`. At a CALL, `*list` / `**dict` spread instead of
collect. Built `make_tag(tag, text, **attrs)` with a comprehension over
`.items()` + `" ".join(...)`.

## Day 34 — 2026-11-02 · 250 XP
**Learned:** `lambda params: expr` = Java's `x -> expr`, but ONE expression
only, returned implicitly (no statements/blocks). Conditional expression:
`a if cond else b` (= `cond ? a : b`, true value first; chains:
`"A" if s >= 85 else "B" if s >= 60 else "C"`). `sorted(xs, key=f,
reverse=True)` returns a new list; `key` decides the ORDER only — the result
holds the original elements (= `Comparator.comparing`). Pass functions
without `()` (`key=len`). Python's sort is stable. `series.apply(f)` calls f
per value → new Series (= `stream().map`); named `def` for multi-line logic.
Prefer vectorized column math when possible — `.apply` is a per-row Python loop.

## Day 33 — 2026-11-01 · 250 XP
**Learned:** Sorting: `df.sort_values("col")` (ascending default;
`ascending=False` for descending); several columns = a list + matching
directions, e.g. `sort_values(["a", "b"], ascending=[True, False])`. Row
labels travel with their rows. Returns a NEW DataFrame (unlike column
assignment). Top-N = `sort_values(...).head(n)`. Ties: default sort isn't
guaranteed stable — use `kind="stable"` or a tie-breaker column.
Counting: `df["col"].value_counts()` → Series of category → count, most
frequent first; `.index[0]` = most common category, `.iloc[0]` = its count;
`normalize=True` → fractions summing to 1; `.sort_index()` orders by label.
String labels sort ALPHABETICALLY (Fri, Mon, Sat…), not by meaning.
**Reflection:** DataFrame-level `value_counts()` counts whole-row combinations — always call
it on a column.

## Day 32 — 2026-11-01 · 250 XP
**Learned:** Filtering rows: a comparison on a column → boolean Series;
`df[mask]` keeps matching rows, all columns, ORIGINAL row labels (not
renumbered). Combine with `&` / `|` / `~` and `()` around comparisons. `|`
keeps each row at most once — filters never duplicate. `df.loc[mask, "col"]`
= filter rows + pick a column. New columns: `df["new"] = <vectorized expr>`
(like SQL `SELECT *, a - b AS new`); combine columns row by row; boolean
columns work as flags (`~df["flag"]`). Assignment MODIFIES the DataFrame in
place; reusing a name overwrites the column. The index isn't a column.

## Day 31 — 2026-10-29 · 250 XP
**Learned:** pandas DataFrame — a 2D table with labeled rows (index) AND
columns; each column is a Series, columns can differ in type. Build from a
dict of lists (key = column name). `.shape` (rows, cols), `.columns`,
`.dtypes`, `.head(n)`. Text columns are `str` in pandas 3 (`object` in older
versions/tutorials). Select: `df["col"]` → Series; `df[["a", "b"]]` →
DataFrame (a LIST of names; one name in a list still gives a DataFrame).
Rows/cells: `.loc[row_label, "col"]` (label, slice inclusive) and
`.iloc[row_pos, col_pos]` (positions, zero-based, exclusive). Row first, always.

## Day 30 — 2026-10-27 · 250 XP
**Learned:** pandas begins (`import pandas as pd`). A Series = a 1D NumPy
array + labels (the index) — like an ordered `LinkedHashMap` with vectorized
math. `pd.Series(values, index=[...])`; no index → 0, 1, 2… Prints labels
down the left + a `dtype` line (that's how you tell it from a bare array).
NumPy ops, masks and aggregations all work and keep the labels. `.loc[label]`
= by label (`map.get`), `.iloc[i]` = by position, zero-based (`list.get`).
Position slices are end-EXCLUSIVE; label slices are end-INCLUSIVE. Integer →
plain value; slice → a Series (keeps the dimension). Missing label → KeyError.

## Day 29 — 2026-10-26 · 300 XP (incl. bonus)
**Built:** NumPy consolidation — a study-app usage report. Flat data →
`reshape(4, -1)`; seven pure functions (take array, return result, no
printing, no loops) using axis aggregations, masks, broadcasting + keepdims;
composed (`weekly_share` reuses `user_totals`). Plus 2 pytest tests.
**Learned:** Parameter SHADOWING — a param with the same name as a module
variable hides it; give them different names (`usage` vs `usage_minutes`).
A DEFAULT lives in the definition (`def f(x, threshold=30)`); a KEYWORD
ARGUMENT at the call site (`f(x, threshold=30)`) only names it. `argmax` with
no axis on a (4,1) column returns a flattened index — sum to 1D first.

## Day 28 — 2026-10-25 · 250 XP
**Learned:** Array creation & reshape. `np.arange(start, stop, step)` = range()
returning an array (= `for (i = start; i < stop; i += step)`, end-exclusive;
one arg → starts at 0). `np.zeros` / `np.ones` → FLOATS by default; 2D shape
is a tuple → double parens `np.zeros((2, 3))`. `.reshape(r, c)` rearranges
the same data, filling row by row; element count must match (check `.size`
first, else ValueError). `-1` = infer that dimension (must divide evenly);
`.reshape(-1, 1)` → column vector, common in ML. Returns a NEW array —
capture it. (2, 2, 3) = 3D: 2 blocks of 2×3 grids.


## Day 27 — 2026-10-25 · 250 XP
**Learned:** Broadcasting — NumPy stretches arrays of different shapes to fit
(no actual copy). Rule: line shapes up from the RIGHT; each pair must be equal
or one must be 1; a missing position counts as 1. (2,3) + (3,) works — the row
is reused for every row. (2,3) + (2,) fails — 3 vs 2, even though there are 2
rows. A column vector (n,1) stretches across columns → one value per row.
`keepdims=True` keeps the collapsed axis as size 1: `sum(axis=1, keepdims=True)`
→ (4,1), which is what makes per-row division broadcast. Used it for
per-feature centering `x - x.mean(axis=0)` and row-normalizing `x / x.sum(...)`.

## Day 26 — 2026-10-23 · 250 XP
**Learned:** Axis-wise aggregations. `axis` = the dimension that gets
COLLAPSED (its position in the shape tuple). Shape (4, 3): `axis=0` squashes
rows → one result per column, shape (3,); `axis=1` squashes columns → one per
row, shape (4,); no axis → one number. Cross-out trick: remove the axis from
the shape to get the result's shape. Works for sum/mean/max/min/argmax.
Masking 2D → flat 1D result. Mask + axis = counts per row/column:
`(m > 5).sum(axis=1)`. Whatever is left of `.sum()` gets summed — a mask
gives COUNTS, values give TOTALS. `max` = value, `argmax` = index.

## Day 25 — 2026-10-23 · 250 XP
**Learned:** Boolean masking. Comparisons are element-wise: `arr > 80` →
a boolean array, same shape. `arr[mask]` keeps elements where the mask is
True → a new, shorter 1D array (= Java stream `.filter()`, no loop).
Combine conditions with `&` / `|` / `~` — NOT `and`/`or`/`not` (those raise
ValueError on arrays). Each condition needs its own `()` because `&` binds
tighter than `>`. True = 1, so `mask.sum()` COUNTS matches; `arr[mask].sum()`
TOTALS the values — different questions. No match → empty array `[]`.

## Day 24 — 2026-10-21 · 250 XP
**Learned:** 2D arrays — built from a list of lists, one inner list per row.
Unlike Java's jagged `int[][]`, a NumPy grid is one rectangular memory block.
`.shape` = (rows, cols) tuple; `.ndim` = dimensions (= leading brackets);
`.size` = total elements. `(3,)` is 1D (comma makes the tuple); `(1, 3)` is a
row vector; `(3, 1)` is a column vector. Indexing: `m[row, col]` — left of
comma = rows, right = columns. `m[:, 1]` = a whole column (no loop). Slices are
end-exclusive (count = end − start). Integer index DROPS a dimension
(`m[0]` → shape (3,)); a slice KEEPS it (`m[:1]` → shape (1, 3)).

## Day 23 — 2026-10-20 · 250 XP
**Learned:** Phase 2 begins — NumPy. `import numpy as np` (universal alias).
`ndarray` = Java's `double[]`: one type, packed in memory, math runs in C.
Same operator, different meaning by type: list `+`/`*` = concatenate/repeat;
array `+`/`*` = element-wise math (NumPy overloads `__add__`/`__mul__`).
Print tells: commas = list, spaces = array; trailing dot (`10.`) = float.
`/` always floats; `//` keeps ints. Aggregations squash to one value:
`.sum()`, `.mean()` (float), `.max()`, `.min()`, `.argmax()`/`.argmin()`
(the INDEX, not the value). Vectorization: element-wise op + aggregation,
no loops. `x - x.mean()` = centering (value minus mean, sign matters).

## 🏆 PHASE 1 BOSS CLEARED — 2026-10-19
Built a CLI Task Manager from scratch, no scaffolding: Task + TaskManager classes,
file persistence (round-trips across runs tasks persists and loads back in the form of tasks), IndexError + ValueError handling, 5 passing pytest tests (incl. save/load round-trip), interactive CLI loop. Debugged 7 issues from first draft unaided. Derive-don't-store applied twice. Bonus: handled non-numeric input without being asked.


## Day 21 — 2026-10-18 · 250 XP
**Learned:** pytest — first genuinely new skill. Test = plain function, named
`test_*` in a `test_*.py` file (naming IS registration, no @Test/class). Use
built-in `assert expr` (no assertEquals). Run with bare `pytest` — auto-discovers
all tests. Dots = passes; failures show actual-vs-expected diff automatically.
`with pytest.raises(ErrorType):` tests that code raises the right error (here the
error is SUCCESS, inverted from normal code). This is the boss's "tested" requirement.
**Reflection:** Far less ceremony than JUnit. The raises-block inversion (error =
pass) is the one mental flip.

## Day 20 — 2026-10-17 · 250 XP
**Learned:** String methods — `.split(sep)`/`.join()` (inverses; join's separator
owns the method), `.strip()`, `.lower()`/`.upper()`, `.replace()`, `.startswith()`/
`.endswith()`, `in`. Key rule: strings are IMMUTABLE — every method returns a NEW
string, original untouched; capture with `s = s.method()` or lose it. Built a text
cleaner: `.split(",")` + comprehension chaining `.strip().lower()` per piece — the
pure-Python version of a pandas data-cleaning op.
**Reflection:** Immutability trap (expecting s to change) is the one to watch.
Method-chaining inside a comprehension came out clean first try.

## Day 19 — 2026-10-17 · 200 XP
**Learned:** Dict iteration — loop keys (default), `.values()`, `.items()` (gives
(k,v) tuples to unpack = Java entrySet but lighter). `.split()` breaks a string
into a word list. Biggest build yet (WordCounter): `.get(word,0)+1` replaces an
if/else for new-vs-seen words; method calling method (`self.add_word`); file load
+ FileNotFoundError. Bug (twice, same kind): forgot `return` — silent None from
Day 8, surfaced far from its cause (c.report() quietly didn't run). Lesson: every
value-producing path must actually return.
**Reflection:** Five concepts woven, architecture right both passes. Only misses
were missing returns — the quiet failure mode, now felt in a real program.

## Day 18 — 2026-10-17 · 175 XP
**Learned:** A class that OWNS a collection — `self.expenses = [] \\initializing an empty list` as a field,
`add`/`total`/`show_all` operating across it. New shape: object manages state +
offers operations (the backbone of real programs). Built from a full spec in one
go (less scaffolding). Bug: called a method as a free function `total(self)` —
methods are reached THROUGH the object: `self.total()`. Mirror of Day 17's
free-function-no-self. Also: Python uses snake_case (`show_all`) not camelCase.


## Day 17 — 2026-10-15 · 225 XP
**Learned:** First INTEGRATED build — classes + file I/O + exceptions in one
program (a note-saver). Key wins: `str(self)` to reuse `__str__` inside another
method (composition); append mode `"a"` vs read `"r"`; catching the error type
that actually fires (`FileNotFoundError`, not a reflexive ValueError); `load_notes`
as a free function (no self). Caught the self-on-free-function trap this time.
Bug fixed early: `length = ...` (local, dies) vs `self.length = ...` (persists).


## Day 16 — 2026-08-13 · 250 XP
**Learned:** File I/O — `open(path, mode)`, modes `"w"` (overwrite), `"r"` (read,
default), `"a"` (append). `with open(...) as f:` = try-with-resources — guaranteed
close, no `f.close()` needed. `write` does NOT add `\n` (unlike print) — add it
yourself. Lines READ from a file carry their trailing `\n`, so `.strip()` before
printing/comparing or comparisons silently fail. `for line in f:` iterates a file
line by line (memory-efficient).


## Day 15 — 2026-08-13 · 250 XP
**Learned:** Module system — every `.py` file is a module named by its filename.
Three import forms: `import mod` (use `mod.name`), `from mod import name` (use bare),
`from mod import a, b`. No class requirement — import functions/vars/classes directly.
`__name__` is `"__main__"` when run directly, the module name when imported — so
`if __name__ == "__main__":` holds run-directly test code. Scope catch: a function's
parameters don't exist outside it.


## Day 14 — 2026-08-13 · 250 XP
**Learned:** Exceptions — `try:` / `except ErrorType:` = try/catch. `except` catches
the type you name, lets others propagate. `as e` binds the error object; `finally`
always runs; `raise` = throw. Key distinction: `raise` = I
produce the error signal; `except` = I react to one. This exercise was pure react.


## Day 13 — 2026-08-11 · 250 XP
**Learned:** Dunder methods — Python calls specially-named methods when things
happen to your object. `__str__` = `toString()` (must RETURN a string, never
print). `__eq__(self, other)` = `equals()`, wired to the `==` operator; default
`==` compares identity like Java, override to compare contents. Dunders = operator
overloading, which Java lacks (`__add__` → `+`, etc.). `__init__` was my first one.


## Day 12 — 2026-08-11 · 250 XP
**Learned:** Inheritance — `class Child(Parent):` = extends, overrides automatic
(no @Override), `super().__init__(...)` = Java's `super(...)` for constructor
chaining. Methods return values like functions. Key catch: methods must READ
`self.field`, not hardcode literals — that's what makes one method describe any
instance (polymorphism). Child inherits parent's `__init__` if it defines none.


## Day 11 - 2026-07-30 - Classes
*Learned*: Class declaration, __init__ is the constructor. 'self' should be the first parameter of every method. Eg: self.varName = something, varName need not be declared before hand, the varName will come into existence as soon as self.varName line executes


## Day 10 - 2026-07-29 - Dictionary/Set Comprehension and f-strings
*Learned*: Comprehension brackets as per container. list - [v ...], dict - {k:v ...}, set{v ...}
f-strings: f".... {expr}.." anything inside the curly braces gets evaluated and converted to a string, auto converts type. {val:.2f} / {val:.1%} for formatting


## Day 9 - 2026-07-28 - List Comprehension
*Learned*: List comprehension: '[expr for var in source if condition]'. Java's map, filter and collect has been folded into simple bracket syntax. It's an expression that evaluates to a whole list. While writing we have transformation first but execution sequence follows the flow: condition -> transform. append() grows a list

## Day 8 - 2026-07-27 - Functions
*Learned*: Function and their declaration. No 'void', function without 'return' will returns 'None' silently. Default arguments in method declaration. '**' means exponentiation. '//' is floor division and '%' is remainder. Multiple return values of method are unpacked at their calling site.


## Day 7 - 2026-07-26 - Control flow
*Learned*: 'if/elif/else' with colon and indent syntax. 'and' 'or' 'not' = '&&', '||', '!'
for loop is by default for each, python iterates on elements and not index. enumerate returns index and value as an unpackable pair. range(N) iterates the loop over 'N' times, end exclusive. while is same as java  
**Reflection** We are iterating over values and not indices. 


## Day 6 - 2026-07-25 - Tuples, unpacking, '//' vs '/'
*Learned*: 'tuple' = immutable sequence(list) '(....)'. Index/slices works like a list, but
can't mutate. slicing a tuple returns a tuple. There are three uses:
multiple return values. ('return a, b' packs a tuple, 'x,y' = unpacks the value from function)
Dict keys must be immutable and signalling "fixed group". Python '/' is ALWAYS float (17/5 = 3.4)
Use '//' for integer floor division
**Reflection** Unpacking multiple return values is cleaner than Java's wrapper classes.
The '/' vs '//' thing will burn if not careful.

## Day 5 - 2026-07-24 - Dict and Set
*Learned:* 'dict' = 'HashMap' with '{key, value} literals, bracket lookup.
Missing Key -> 'KeyError' (loud) throws error when key is not present, vs Java's silent 'null', 'get()' opts looks into Java-style default ('None' or or a fallback(custom default value) you supply)
'set' = 'HashSet' with {'a', 'b'} literals, duplicates don't exist. 
'{}' means an empty *dict*, empty set is denoted by 'setName()'. And as java returns null, Python returns None.
*Reflection:* dict/set really are HashMap/HashSet 

## Day 4 - 2026-07-23 - List and Slicing

## Day 3 - 2026-07-22 - Dynamic Typing

## Day 2 — 2026-07-16 · 250 XP · Streak 2
*Learned:* Python has no classpath — sys.path is per-interpreter, so venvs
isolate by giving each project its own interpreter. pip freeze is the lockfile;
requirements.txt in, .venv/ out — same rule as pom.xml in, target/ out.
*Reflection:* The isolation problem is identical to Maven's. The solution is
inverted, and the inversion is the whole lesson.

## Day 1 — 2026-07-15 · 150 XP · Streak 1
*Learned:* Python executes files top-to-bottom; def is a binding, not a
declaration. Indentation is the block structure.
*Reflection:* Two wrong predictions taught me more than a right one would have.