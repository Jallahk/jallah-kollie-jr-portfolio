const statsGrid = document.getElementById("stats-grid");
const searchInput = document.getElementById("search-input");
const missingFoldersNote = document.getElementById("missing-folders-note");
const demoGrid = document.getElementById("demo-grid");
const demoCount = document.getElementById("demo-count");
const demoForm = document.getElementById("demo-form");
const modalBackdrop = document.getElementById("project-modal-backdrop");
const modalCloseButton = document.getElementById("project-modal-close");
const modalFolder = document.getElementById("project-modal-folder");
const modalTitle = document.getElementById("project-modal-title");
const modalSummary = document.getElementById("project-modal-summary");
const modalMeta = document.getElementById("project-modal-meta");
const modalSource = document.getElementById("project-modal-source");
const modalCode = document.getElementById("project-modal-code");

const PAGE_SIZE = 10;

const tabSections = {
  "Machine Learning": {
    button: document.getElementById("tab-machine-learning"),
    panel: document.getElementById("panel-machine-learning"),
    grid: document.getElementById("project-grid-machine-learning"),
    count: document.getElementById("results-count-machine-learning"),
    prev: document.getElementById("prev-machine-learning"),
    next: document.getElementById("next-machine-learning"),
    pageInfo: document.getElementById("page-info-machine-learning"),
  },
  "A&D": {
    button: document.getElementById("tab-a-d"),
    panel: document.getElementById("panel-a-d"),
    grid: document.getElementById("project-grid-a-d"),
    count: document.getElementById("results-count-a-d"),
    prev: document.getElementById("prev-a-d"),
    next: document.getElementById("next-a-d"),
    pageInfo: document.getElementById("page-info-a-d"),
  },
};

const DEMO_DB_NAME = "jallah-kollie-jr-portfolio-demos";
const DEMO_STORE = "demos";

let catalog = [];
let currentPages = {
  "Machine Learning": 1,
  "A&D": 1,
};

const formatNumber = (value) => new Intl.NumberFormat().format(value);

const createStatCard = (label, value) => {
  const card = document.createElement("article");
  card.className = "stat-card";
  card.innerHTML = `<p>${label}</p><strong>${value}</strong>`;
  return card;
};

const renderStats = (data) => {
  statsGrid.innerHTML = "";
  const totalLines = data.files.reduce((sum, item) => sum + item.line_count, 0);
  const sectionsPresent = data.sections.filter((section) => section.available).length;

  [
    ["Python Files", formatNumber(data.files.length)],
    ["Folders Included", formatNumber(sectionsPresent)],
    ["Lines of Code", formatNumber(totalLines)],
    ["Latest Update", data.latest_modified_label],
  ].forEach(([label, value]) => {
    statsGrid.appendChild(createStatCard(label, value));
  });
};

const renderMissingFolders = (sections) => {
  const missing = sections.filter((section) => !section.available).map((section) => section.name);
  missingFoldersNote.textContent = missing.length
    ? `Folder note: ${missing.join(", ")} was not found on disk when this portfolio was generated, so it is not shown yet.`
    : "All requested folders were found when this portfolio was generated.";
};

const openProjectModal = (item) => {
  modalFolder.textContent = item.section;
  modalTitle.textContent = item.title;
  modalSummary.textContent = item.summary;
  modalSource.href = item.file_url;
  modalCode.textContent = item.preview;

  modalMeta.innerHTML = "";
  [
    item.relative_path,
    `${item.line_count} lines`,
    item.modified_label,
    item.size_label,
  ].forEach((text) => {
    const chip = document.createElement("span");
    chip.textContent = text;
    modalMeta.appendChild(chip);
  });

  modalBackdrop.classList.remove("hidden");
  document.body.style.overflow = "hidden";
};

const closeProjectModal = () => {
  modalBackdrop.classList.add("hidden");
  document.body.style.overflow = "";
};

const getFilteredItems = (sectionName) => {
  const term = searchInput.value.trim().toLowerCase();
  return catalog.filter((item) => {
    if (item.section !== sectionName) {
      return false;
    }
    const haystack = [
      item.title,
      item.relative_path,
      item.summary,
      ...item.tags,
    ].join(" ").toLowerCase();
    return !term || haystack.includes(term);
  });
};

const renderPagination = (sectionName, totalItems) => {
  const section = tabSections[sectionName];
  const totalPages = Math.max(1, Math.ceil(totalItems / PAGE_SIZE));
  const currentPage = Math.min(currentPages[sectionName], totalPages);
  currentPages[sectionName] = currentPage;

  section.pageInfo.textContent = `Page ${currentPage} of ${totalPages}`;
  section.prev.disabled = currentPage === 1;
  section.next.disabled = currentPage === totalPages;
};

const renderCardsForSection = (sectionName) => {
  const section = tabSections[sectionName];
  const filtered = getFilteredItems(sectionName);
  const totalPages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));

  if (currentPages[sectionName] > totalPages) {
    currentPages[sectionName] = totalPages;
  }

  const currentPage = currentPages[sectionName];
  const startIndex = (currentPage - 1) * PAGE_SIZE;
  const visibleItems = filtered.slice(startIndex, startIndex + PAGE_SIZE);

  section.count.textContent = `${formatNumber(filtered.length)} files shown`;
  section.grid.innerHTML = "";
  renderPagination(sectionName, filtered.length);

  if (!filtered.length) {
    section.grid.innerHTML = `<div class="empty-state">No files matched that search in this tab.</div>`;
    return;
  }

  visibleItems.forEach((item) => {
    const card = document.createElement("article");
    card.className = "project-card";
    card.dataset.id = item.id;
    card.innerHTML = `
      <p class="card-folder">${item.section}</p>
      <h3>${item.title}</h3>
      <p class="card-summary">${item.summary}</p>
      <div class="card-meta">
        <span>${item.relative_path}</span>
        <span>${item.line_count} lines</span>
        <span>${item.size_label}</span>
      </div>
    `;
    card.addEventListener("click", () => openProjectModal(item));
    section.grid.appendChild(card);
  });
};

const renderAllCodeTabs = () => {
  Object.keys(tabSections).forEach(renderCardsForSection);
};

const activateTab = (tabName) => {
  document.querySelectorAll(".tab-button").forEach((button) => {
    button.classList.toggle("active", button.dataset.tab === tabName);
    button.setAttribute("aria-selected", String(button.dataset.tab === tabName));
  });
  document.querySelectorAll(".tab-panel").forEach((panel) => {
    panel.classList.toggle("active", panel.id === `panel-${tabName.toLowerCase().replace(/[^a-z0-9]+/g, "-")}`);
  });
};

const goToPage = (sectionName, direction) => {
  currentPages[sectionName] += direction;
  renderCardsForSection(sectionName);
};

const resetPagesAndRender = () => {
  Object.keys(currentPages).forEach((sectionName) => {
    currentPages[sectionName] = 1;
  });
  renderAllCodeTabs();
};

const openDemoDatabase = () => new Promise((resolve, reject) => {
  const request = window.indexedDB.open(DEMO_DB_NAME, 1);
  request.onerror = () => reject(request.error);
  request.onupgradeneeded = () => {
    const db = request.result;
    if (!db.objectStoreNames.contains(DEMO_STORE)) {
      db.createObjectStore(DEMO_STORE, { keyPath: "id" });
    }
  };
  request.onsuccess = () => resolve(request.result);
});

const getSavedDemos = async () => {
  const db = await openDemoDatabase();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(DEMO_STORE, "readonly");
    const store = tx.objectStore(DEMO_STORE);
    const request = store.getAll();
    request.onerror = () => reject(request.error);
    request.onsuccess = () => resolve(request.result || []);
  });
};

const saveDemo = async (demo) => {
  const db = await openDemoDatabase();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(DEMO_STORE, "readwrite");
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
    tx.objectStore(DEMO_STORE).put(demo);
  });
};

const deleteDemo = async (id) => {
  const db = await openDemoDatabase();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(DEMO_STORE, "readwrite");
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
    tx.objectStore(DEMO_STORE).delete(id);
  });
};

const createDemoMarkup = (demo) => {
  if (demo.videoBlob) {
    const videoUrl = URL.createObjectURL(demo.videoBlob);
    return `
      <video controls preload="metadata">
        <source src="${videoUrl}">
        Your browser does not support the video tag.
      </video>
    `;
  }

  if (demo.video_url) {
    return `
      <video controls preload="metadata">
        <source src="${demo.video_url}">
        Your browser does not support the video tag.
      </video>
    `;
  }

  return `<div class="demo-placeholder"><div><strong>Demo placeholder</strong><p>${demo.status || "Private demo"}</p></div></div>`;
};

const renderDemos = async (seedDemos = []) => {
  const savedDemos = await getSavedDemos().catch(() => []);
  const demos = [...savedDemos, ...seedDemos.map((demo, index) => ({ ...demo, id: demo.id || `seed-${index}` }))];

  demoGrid.innerHTML = "";
  demoCount.textContent = `${formatNumber(demos.length)} demos`;

  if (!demos.length) {
    demoGrid.innerHTML = `<div class="empty-state">No demos yet. Use the form above to add a video, description, and link whenever you want.</div>`;
    return;
  }

  demos.forEach((demo) => {
    const card = document.createElement("article");
    card.className = "demo-card";
    const liveLink = demo.projectUrl || demo.project_url
      ? `<a class="button secondary" href="${demo.projectUrl || demo.project_url}" target="_blank" rel="noreferrer">Project Link</a>`
      : "";

    const removable = !String(demo.id).startsWith("seed-")
      ? `<button class="button secondary remove-button" type="button" data-demo-id="${demo.id}">Remove Demo</button>`
      : "";

    card.innerHTML = `
      ${createDemoMarkup(demo)}
      <span class="demo-status">${demo.status || "Private demo"}</span>
      <h3>${demo.title}</h3>
      <p class="card-summary">${demo.description}</p>
      <div class="demo-links">${liveLink}</div>
      ${removable}
    `;

    demoGrid.appendChild(card);
  });

  demoGrid.querySelectorAll("[data-demo-id]").forEach((button) => {
    button.addEventListener("click", async () => {
      await deleteDemo(button.dataset.demoId);
      renderDemos(seedDemos);
    });
  });
};

const handleDemoSubmit = async (event) => {
  event.preventDefault();
  const formData = new FormData(demoForm);
  const videoFile = formData.get("video");

  const demo = {
    id: `demo-${Date.now()}`,
    title: String(formData.get("title") || "").trim(),
    description: String(formData.get("description") || "").trim(),
    status: String(formData.get("status") || "").trim() || "Private demo",
    projectUrl: String(formData.get("projectUrl") || "").trim(),
  };

  if (videoFile instanceof File && videoFile.size > 0) {
    demo.videoBlob = videoFile;
  }

  await saveDemo(demo);
  demoForm.reset();
  renderDemos(window.PORTFOLIO_DATA?.demos || []);
};

if (window.PORTFOLIO_DATA) {
  const data = window.PORTFOLIO_DATA;
  catalog = data.files;
  renderStats(data);
  renderMissingFolders(data.sections);
  renderAllCodeTabs();
  renderDemos(data.demos || []);
} else {
  Object.values(tabSections).forEach((section) => {
    section.count.textContent = "Portfolio data could not be loaded.";
    section.grid.innerHTML = `<div class="empty-state">The project catalog is missing.</div>`;
  });
  demoGrid.innerHTML = `<div class="empty-state">Demo data could not be loaded.</div>`;
}

document.querySelectorAll(".tab-button").forEach((button) => {
  button.addEventListener("click", () => activateTab(button.dataset.tab));
});

Object.entries(tabSections).forEach(([sectionName, section]) => {
  section.prev.addEventListener("click", () => goToPage(sectionName, -1));
  section.next.addEventListener("click", () => goToPage(sectionName, 1));
});

searchInput.addEventListener("input", resetPagesAndRender);
demoForm.addEventListener("submit", handleDemoSubmit);
modalCloseButton.addEventListener("click", closeProjectModal);
modalBackdrop.addEventListener("click", (event) => {
  if (event.target === modalBackdrop) {
    closeProjectModal();
  }
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !modalBackdrop.classList.contains("hidden")) {
    closeProjectModal();
  }
});
