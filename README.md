# 🌟 DFS Visualization GUI

This project provides a graphical user interface (GUI) application for visualizing Depth-First Search (DFS) on directed graphs. It offers an intuitive way to explore graph traversal, with features designed for ease of use and flexibility.

---

## 🚀 Features

- 📂 **Load Graphs**: Import graphs from a JSON file.
- 🔍 **Graph Selection**: Choose from a list of loaded graphs.
- 🎯 **Custom Start Node**: Define a starting node for DFS traversal.
- 📈 **Real-Time Visualization**: Watch the DFS traversal unfold on the graph.
- ⚠️ **Error Handling**: Get notifications for cycles or invalid nodes.

---

## 🛠️ Requirements

Ensure you have the following installed:

- **Python** 3.x
- **Libraries**: 
  - `tkinter`
  - `matplotlib`
  - `networkx`

---

## ⚙️ Setup

### 1️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
```

Activate the environment according to your operating system:
- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 📖 Usage

Ensure your JSON file follows this structure:

```json
{
    "Graph1": [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6]],
    "Graph2": [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],
    "Tree1": [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
}
```

- Each graph is represented as a dictionary key, with edges defined as pairs of nodes.
- **Example**: `"Graph1": [[0, 1], [0, 2]]` defines edges `0 → 1` and `0 → 2`.

---

