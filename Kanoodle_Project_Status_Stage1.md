# Kanoodle Challenge – Project Status & Architecture Overview

> *Everything you need to on‑board the next contributor or AI session.*

---

## 📁 Current Repo Layout
```
kanoodle-challenge/
├─ assets/
├─ puzzle/
│  ├─ pieces.py
│  ├─ piece.py
│  ├─ orient.py
│  └─ board.py
├─ sandbox/main.py
├─ tests/test_orient.py
└─ Summary.md
```

---

## 1️⃣ Piece Data Model
```python
@dataclass(frozen=True)
class Piece:
    piece_id: int
    name: str
    label: str
    size: int
    coords: List[Coord]
    orientations: List[List[Coord]] = field(default_factory=list, repr=False)
    bounding_boxes: List[Tuple[int,int]] = field(default_factory=list, repr=False)
```
*Immutable → hash‑safe; orientation data is patched in once at load time.*

---

## 2️⃣ Orientation Generator
* `mirror_y`, `rotate_ccw`, `_normalise`
* `generate_orientations(base)` loops over mirror & rotation, deduplicates via `seen`, returns `(orientations, bounding_boxes)`.

---

## 3️⃣ Board Engine
```python
b = Board()
b.place_ori("Orange", 3, 0, 0)
b.remove_piece("Orange")
print(b)
```
* `self.grid` 5×11
* `self.pieces` dict of fully‑populated `Piece`
* `self.placed` remembers `(orient_id,row,col)` for removal.

---

## 4️⃣ Tests
`tests/test_orient.py` ensures mirrored pose appears in orientation list.

---

## 5️⃣ What Works
* All pieces load with correct unique orientations.
* Placement & removal safe for any pose.
* Sandbox driver playable.

---

## 6️⃣ Next Steps
1. Wrap `Board` in a Gymnasium environment with action masks.
2. Add reward shaping (+α per new square, +1 on complete solve).
3. Curriculum: start with small boards / piece subsets.
4. Optional bit‑board speed‑ups.
5. Visualiser for AI runs.
6. Add pytest + CI.

---

## 7️⃣ Files to Provide
```
puzzle/pieces.py
puzzle/piece.py
puzzle/orient.py
puzzle/board.py
sandbox/main.py
tests/test_orient.py
```

**Prompt for new chat**

> “Here’s the current Kanoodle solver implementation (files attached). Help me turn `Board` into a Gym environment with action masks and reward shaping.”
