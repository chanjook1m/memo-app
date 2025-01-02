async function editMemo(e) {
  const id = e.target.dataset.id;
  const editInput = prompt("새 값을 입력하세요");

  const res = await fetch(`/api/memos/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id, content: editInput }),
  });

  readMemos();
}

async function deleteMemo(e) {
  const id = e.target.dataset.id;
  const res = await fetch(`/api/memos/${id}`, {
    method: "DELETE",
  });

  readMemos();
}

function displayMemo(memo) {
  const ul = document.querySelector("#memo-ul");
  const li = document.createElement("li");
  const editButton = document.createElement("button");
  editButton.innerText = "수정";
  const deleteButton = document.createElement("button");
  deleteButton.innerText = "삭제";
  li.textContent = `[id:${memo.id}] ${memo.content}`;

  editButton.addEventListener("click", editMemo);
  editButton.dataset.id = memo.id;
  deleteButton.addEventListener("click", deleteMemo);
  deleteButton.dataset.id = memo.id;
  li.appendChild(editButton);
  li.appendChild(deleteButton);
  ul.appendChild(li);
}

async function readMemos() {
  const res = await fetch("/api/memos");
  const json = await res.json();
  console.log(json);

  const ul = document.querySelector("#memo-ul");
  ul.innerHTML = "";

  json.forEach(displayMemo);
}

async function createMemo(value) {
  const res = await fetch("/api/memos", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id: new Date().getTime(), content: value }),
  });

  const json = await res.json();

  console.log("Memo created: ", json);
  readMemos();
}

function handleSubmit(e) {
  e.preventDefault();
  const input = document.querySelector("#input");
  createMemo(input.value);
  input.value = "";
}

const form = document.querySelector("#form");
form.addEventListener("submit", handleSubmit);

readMemos();
