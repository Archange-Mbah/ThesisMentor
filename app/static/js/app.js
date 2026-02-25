let currentDocId = null;

const pdfFile = document.getElementById("pdfFile");
const uploadBtn = document.getElementById("uploadBtn");
const pdfFrame = document.getElementById("pdfFrame");
const statusEl = document.getElementById("status");

const queryEl = document.getElementById("query");
const askBtn = document.getElementById("askBtn");
const answerEl = document.getElementById("answer");

uploadBtn.addEventListener("click", async () => {
  try {
    if (!pdfFile.files || pdfFile.files.length === 0) {
      statusEl.textContent = "Please choose a PDF first.";
      return;
    }

    statusEl.textContent = "Uploading...";
    const file = pdfFile.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    if (!res.ok) {
      statusEl.textContent = data.error || "Upload failed.";
      return;
    }

    currentDocId = data.doc_id;
    statusEl.textContent = `Upload OK. doc_id=${currentDocId}`;

    // Display the PDF
    pdfFrame.src = data.file_url;
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Upload error. Check console.";
  }
});

askBtn.addEventListener("click", async () => {
  try {
    if (!currentDocId) {
      answerEl.textContent = "Upload a PDF first.";
      return;
    }

    const query = (queryEl.value || "").trim();
    if (!query) {
      answerEl.textContent = "Type a question first.";
      return;
    }

    answerEl.textContent = "Thinking...";

    const res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        doc_id: currentDocId,
        query: query,
      }),
    });

    const data = await res.json();
    if (!res.ok) {
      answerEl.textContent = data.error || "Ask failed.";
      return;
    }

    answerEl.textContent = data.answer;
  } catch (err) {
    console.error(err);
    answerEl.textContent = "Error. Check console.";
  }
});