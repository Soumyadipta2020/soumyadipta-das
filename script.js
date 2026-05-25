(function () {
  const navToggle = document.querySelector(".nav-toggle");
  const tabButtons = Array.from(document.querySelectorAll("[data-tab]"));
  const tabPanels = Array.from(document.querySelectorAll("[data-panel]"));
  const tabLinks = Array.from(document.querySelectorAll("[data-tab-target]"));
  const chartPoints = Array.from(document.querySelectorAll(".chart-point"));
  const tooltip = document.createElement("div");

  tooltip.className = "chart-tooltip";
  tooltip.hidden = true;
  document.body.appendChild(tooltip);

  function setMenuIcon(isOpen) {
    if (!navToggle) {
      return;
    }

    const icon = navToggle.querySelector("svg");
    if (icon) {
      icon.outerHTML = `<i data-lucide="${isOpen ? "x" : "menu"}"></i>`;
    
  // Scroll reveal observer
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.1
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll(".reveal-up").forEach(el => {
    revealObserver.observe(el);
  });

  // Back to Top button logic
  const backToTopBtn = document.getElementById("back-to-top");
  if (backToTopBtn) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.add("is-visible");
      } else {
        backToTopBtn.classList.remove("is-visible");
      }
    });

    backToTopBtn.addEventListener("click", () => {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  }

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

  function scrollToWorkbench() {
    const workbench = document.querySelector(".workbench");
    if (workbench) {
      workbench.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  function showTooltip(point, x, y) {
    tooltip.innerHTML = `<strong>${point.dataset.series}</strong><span>${point.dataset.label}: ${point.dataset.value}%</span>`;
    tooltip.hidden = false;
    tooltip.style.left = `${x}px`;
    tooltip.style.top = `${y}px`;
  }

  function hideTooltip() {
    tooltip.hidden = true;
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
    button.addEventListener("click", (event) => {
      event.preventDefault();
      activateTab(button.dataset.tab);
      closeMenu();
      scrollToWorkbench();
    });
  });

  tabLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      activateTab(link.dataset.tabTarget);
      closeMenu();
      scrollToWorkbench();
    });
  });

  chartPoints.forEach((point) => {
    point.addEventListener("mousemove", (event) => {
      showTooltip(point, event.clientX, event.clientY);
    });

    point.addEventListener("mouseenter", (event) => {
      showTooltip(point, event.clientX, event.clientY);
    });

    point.addEventListener("mouseleave", hideTooltip);

    point.addEventListener("focus", () => {
      const rect = point.getBoundingClientRect();
      showTooltip(point, rect.left + rect.width / 2, rect.top);
    });

    point.addEventListener("blur", hideTooltip);
  });

  const initialTab = window.location.hash.replace("#", "");
  if (initialTab && tabPanels.some((panel) => panel.dataset.panel === initialTab)) {
    activateTab(initialTab);
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
    }
  });


  // Scroll reveal observer
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.1
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll(".reveal-up").forEach(el => {
    revealObserver.observe(el);
  });

  // Back to Top button logic
  const backToTopBtn = document.getElementById("back-to-top");
  if (backToTopBtn) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.add("is-visible");
      } else {
        backToTopBtn.classList.remove("is-visible");
      }
    });

    backToTopBtn.addEventListener("click", () => {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  }

  if (window.lucide) {
    window.lucide.createIcons();
  }
})();
