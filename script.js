(function () {
  const navToggle = document.querySelector(".nav-toggle");
  const tabButtons = Array.from(document.querySelectorAll("[data-tab]"));
  const tabPanels = Array.from(document.querySelectorAll("[data-panel]"));
  const tabLinks = Array.from(document.querySelectorAll("[data-tab-target]"));

  function setMenuIcon(isOpen) {
    if (!navToggle) {
      return;
    }

    const icon = navToggle.querySelector("svg");
    if (icon) {
      icon.outerHTML = `<i data-lucide="${isOpen ? "x" : "menu"}"></i>`;
      if (window.lucide) {
        window.lucide.createIcons();
      }
    }
  }

  function closeMenu() {
    document.body.classList.remove("nav-open");
    if (navToggle) {
      navToggle.setAttribute("aria-expanded", "false");
    }
    setMenuIcon(false);
  }

  function activateTab(tabName) {
    tabButtons.forEach((button) => {
      const isActive = button.dataset.tab === tabName;
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-selected", String(isActive));
    });

    tabPanels.forEach((panel) => {
      const isActive = panel.dataset.panel === tabName;
      panel.classList.toggle("is-active", isActive);
      panel.hidden = !isActive;
    });
  }

  if (navToggle) {
    navToggle.addEventListener("click", () => {
      const isOpen = !document.body.classList.contains("nav-open");
      document.body.classList.toggle("nav-open", isOpen);
      navToggle.setAttribute("aria-expanded", String(isOpen));
      setMenuIcon(isOpen);
    });
  }

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      activateTab(button.dataset.tab);
      const workbench = document.querySelector(".workbench");
      if (workbench) {
        workbench.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });

  tabLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      activateTab(link.dataset.tabTarget);
      closeMenu();
      const workbench = document.querySelector(".workbench");
      if (workbench) {
        workbench.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
    }
  });

  if (window.lucide) {
    window.lucide.createIcons();
  }
})();
