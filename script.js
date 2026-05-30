(function () {
  const navToggle = document.querySelector(".nav-toggle");
  const tabButtons = Array.from(document.querySelectorAll("[data-tab]"));
  const tabPanels = Array.from(document.querySelectorAll("[data-panel]"));
  const tabLinks = Array.from(document.querySelectorAll("[data-tab-target]"));
  const chartPoints = Array.from(document.querySelectorAll(".chart-point"));
  const writingGrid = document.querySelector(".writing-grid");
  const blogReader = document.getElementById("blog-reader");
  const blogArticleContent = document.getElementById("blog-article-content");
  const blogSource = document.getElementById("blog-source");
  const blogBack = document.getElementById("blog-back");
  const blogLinks = Array.from(document.querySelectorAll("[data-blog-id]"));
  const tooltip = document.createElement("div");

  tooltip.className = "chart-tooltip";
  tooltip.hidden = true;
  document.body.appendChild(tooltip);

  const blogArticles = {
    "integrating-sequential-analysis": {
      category: "Data Science",
      date: "January 11, 2025",
      readTime: "6 min read",
      title: "Integrating Sequential Analysis with Time Series Clustering",
      sourceUrl: "https://workramanujan.wordpress.com/2025/01/11/integrating-sequential-analysis-with-time-series-clustering-a-statistical-perspective/",
      dek: "A statistics-first view of how sequential evidence and temporal grouping can work together for monitoring, segmentation, and decision support.",
      tags: ["Sequential Analysis", "Time Series", "Clustering", "Statistics"],
      sections: [
        {
          heading: "Why the combination matters",
          paragraphs: [
            "Sequential analysis is useful when decisions are updated as new observations arrive. Time series clustering is useful when many temporal patterns need to be grouped by shape, rhythm, trend, or volatility. Combining the two creates a workflow where clusters are not only discovered once, but also monitored as evidence changes over time.",
            "This is valuable in forecasting, demand planning, anomaly monitoring, customer behavior, operations, and financial signals where the same group can evolve as fresh data arrives."
          ]
        },
        {
          heading: "A practical workflow",
          paragraphs: [
            "Start by preparing each time series with consistent frequency, missing-value handling, scaling, and feature extraction. Then apply a time-aware distance or representation, such as dynamic time warping, autocorrelation features, rolling statistics, or model-based embeddings.",
            "After the first clustering pass, sequential tests can monitor whether a series still behaves like its assigned cluster or whether evidence suggests a shift. This adds a decision layer on top of the unsupervised grouping."
          ]
        },
        {
          heading: "Statistical safeguards",
          paragraphs: [
            "The main risk is treating noisy movement as a structural change. A good implementation defines stopping rules, controls false alarms, and tracks uncertainty around cluster membership.",
            "The most useful output is not only a cluster label. It is a cluster label with confidence, recent evidence, and a recommendation on whether to keep watching, reassign, or investigate."
          ]
        }
      ]
    },
    "clustering-vs-time-series-clustering": {
      category: "Data Science",
      date: "December 28, 2024",
      readTime: "5 min read",
      title: "The Difference Between Clustering and Time Series Clustering",
      sourceUrl: "https://workramanujan.wordpress.com/2024/12/28/the-difference-between-clustering-and-time-series-clustering-a-statistical-perspective/",
      dek: "A concise guide to why ordinary clustering assumptions often break when the data has order, lag, seasonality, and temporal dependence.",
      tags: ["Clustering", "Time Series", "ML", "Distance Metrics"],
      sections: [
        {
          heading: "Standard clustering",
          paragraphs: [
            "Traditional clustering groups rows based on similarity across variables. Methods such as k-means, hierarchical clustering, and Gaussian mixtures usually assume that each row can be compared as a fixed vector.",
            "That works well for many tabular problems, but it can ignore the order in which values appear. For time-dependent data, order is often the most important part of the signal."
          ]
        },
        {
          heading: "Time series clustering",
          paragraphs: [
            "Time series clustering compares sequences. Two series may be similar even if peaks happen at slightly different times, or they may be different even if their averages are close.",
            "Because of this, time series clustering often uses shape-based, feature-based, or model-based approaches. Dynamic time warping, rolling features, trend and seasonality decomposition, and forecast-model parameters can all help represent temporal behavior."
          ]
        },
        {
          heading: "Choosing the right approach",
          paragraphs: [
            "Use ordinary clustering when the row-level features are enough to describe similarity. Use time series clustering when trend, cycles, lagged response, volatility, or event timing matter.",
            "The decision should come from the business question. If the goal is to group customers by total spend, standard clustering may be enough. If the goal is to group customers by how their spend changes through time, time series clustering is the better frame."
          ]
        }
      ]
    },
    "real-life-time-series-clustering": {
      category: "Data Science",
      date: "December 21, 2024",
      readTime: "5 min read",
      title: "Real-Life Applications of Time Series Clustering",
      sourceUrl: "https://workramanujan.wordpress.com/2024/12/21/real-life-applications-of-time-series-clustering-unlocking-insights-from-temporal-data/",
      dek: "Where temporal clustering becomes useful: demand patterns, patient trajectories, sensor behavior, finance, marketing, and operations.",
      tags: ["Applications", "Forecasting", "Segmentation", "Analytics"],
      sections: [
        {
          heading: "Demand and operations",
          paragraphs: [
            "Retailers, supply chains, and service teams can cluster products, stores, routes, or resources by demand shape. Some series may be seasonal, some may be event-driven, and others may be stable with occasional spikes.",
            "Once those groups are visible, teams can assign different forecasting models, stocking rules, staffing plans, and alert thresholds to each behavior pattern."
          ]
        },
        {
          heading: "Health, finance, and sensors",
          paragraphs: [
            "In healthcare, patient trajectories can be grouped by progression patterns. In finance, assets or accounts can be grouped by volatility and response to market events. In IoT settings, machines can be grouped by normal operating signatures.",
            "The strongest use cases are often monitoring use cases. A series that leaves its expected cluster can become an early signal for intervention."
          ]
        },
        {
          heading: "Marketing and customer analytics",
          paragraphs: [
            "Customer activity is rarely static. Time series clustering can separate newly engaged users, declining users, periodic buyers, campaign responders, and one-time purchasers.",
            "This supports lifecycle targeting, churn prevention, and campaign design because the groups reflect behavior through time rather than a single snapshot."
          ]
        }
      ]
    },
    "optimized-ml-time-series-clustering": {
      category: "Data Science",
      date: "December 14, 2024",
      readTime: "7 min read",
      title: "Steps to Build an Optimized ML Model for Time Series Clustering",
      sourceUrl: "https://workramanujan.wordpress.com/2024/12/14/steps-to-build-an-optimized-machine-learning-model-for-time-series-clustering/",
      dek: "A practical build path for turning raw temporal data into reliable clusters that can be evaluated, explained, and used.",
      tags: ["ML Workflow", "Modeling", "Validation", "Time Series"],
      sections: [
        {
          heading: "Prepare the data",
          paragraphs: [
            "Begin with frequency alignment, duplicate handling, missing-value treatment, and outlier review. Time series clustering is sensitive to inconsistent measurement intervals, so the data foundation matters as much as the algorithm.",
            "Normalize or scale series when the question is about shape. Keep the original scale when magnitude is part of the business meaning."
          ]
        },
        {
          heading: "Build useful representations",
          paragraphs: [
            "Raw values are only one representation. You can also cluster on lag features, rolling means, trend strength, seasonality, volatility, autocorrelation, change points, or embeddings from time series models.",
            "The best representation is the one that preserves the behavior you want the cluster to capture."
          ]
        },
        {
          heading: "Evaluate and operationalize",
          paragraphs: [
            "Internal metrics such as silhouette score, Davies-Bouldin index, and cluster stability are useful, but they are not enough. Clusters should also be inspected visually and validated against domain expectations.",
            "After deployment, monitor drift, membership changes, and downstream decisions. A clustering model is successful when the segments remain interpretable and useful in real workflows."
          ]
        }
      ]
    },
    "gomukh-tapovan-guide": {
      category: "Travel",
      date: "March 9, 2025",
      readTime: "6 min read",
      title: "Discovering the Mystical Beauty of Gomukh and Tapovan",
      sourceUrl: "https://workramanujan3.wordpress.com/2025/03/09/discovering-the-mystical-beauty-of-gomukh-and-tapovan-a-complete-travel-guide/",
      dek: "A high-altitude guide to the Gangotri, Gomukh, and Tapovan trail with route planning, permits, altitude awareness, and practical travel notes.",
      tags: ["Himalayas", "Gomukh", "Tapovan", "Travel Guide"],
      sections: [
        {
          heading: "The route",
          paragraphs: [
            "The journey usually begins at Gangotri and moves through Chirbasa and Bhojbasa toward Gomukh, the glacier snout associated with the origin of the Bhagirathi. Tapovan sits higher above Gomukh and is known for wide meadows, severe terrain, and dramatic views of Shivling and surrounding peaks.",
            "This is not a casual walk. The altitude, weather, moraine sections, and limited facilities make preparation essential."
          ]
        },
        {
          heading: "Planning essentials",
          paragraphs: [
            "Permits are required for the protected Gangotri National Park area, and daily entry limits can apply. A guide is strongly recommended, especially for the Gomukh to Tapovan section where the path can change with conditions.",
            "The best windows are generally pre-monsoon and post-monsoon, depending on snow, road access, and local advisories. Keep buffer days because mountain weather can change plans quickly."
          ]
        },
        {
          heading: "Travel mindset",
          paragraphs: [
            "Move slowly, hydrate, and respect acclimatization. The beauty of the route is tied to its fragility, so avoid litter, stay on permitted trails, and follow local guidance.",
            "Gomukh and Tapovan reward patience. The experience is less about rushing to a point and more about absorbing the scale, silence, and discipline of the high Himalayas."
          ]
        }
      ]
    },
    "kedarnath-guide": {
      category: "Travel",
      date: "February 23, 2025",
      readTime: "5 min read",
      title: "Kedarnath: Abode of Shiva in the Majestic Himalayas",
      sourceUrl: "https://workramanujan3.wordpress.com/2025/02/23/kedarnath-abode-of-shiva-in-the-majestic-himalayas/",
      dek: "A practical and devotional guide to Kedarnath, covering access, route expectations, weather, and travel preparation.",
      tags: ["Kedarnath", "Uttarakhand", "Pilgrimage", "Travel"],
      sections: [
        {
          heading: "The journey",
          paragraphs: [
            "Kedarnath is one of the most revered Himalayan pilgrimage destinations. The temple sits in a dramatic valley surrounded by high peaks, and the approach combines road travel, registration, weather checks, and a steep final trek from the base area.",
            "The trek can feel very different depending on season, crowd, rain, snow, and personal fitness."
          ]
        },
        {
          heading: "Before you go",
          paragraphs: [
            "Register as required by current Char Dham guidelines, check weather and route advisories, and keep warm layers, rain protection, basic medicines, and identity documents ready.",
            "Accommodation can fill quickly in peak season. Booking early and keeping a backup plan helps avoid stress after a long travel day."
          ]
        },
        {
          heading: "On the trail",
          paragraphs: [
            "Start early, pace yourself, and avoid underestimating altitude and cold. Horses, palanquins, and helicopter services may be available, but they depend on weather, operations, and availability.",
            "Kedarnath is both a physical journey and a spiritual one. Keeping the route clean and respecting local systems makes the pilgrimage better for everyone."
          ]
        }
      ]
    },
    "tunganath-guide": {
      category: "Travel",
      date: "January 12, 2025",
      readTime: "5 min read",
      title: "Exploring Tunganath: A Complete Travel Guide",
      sourceUrl: "https://workramanujan3.wordpress.com/2025/01/12/exploring-tunganath-a-complete-travel-guide/",
      dek: "A compact guide to reaching Tunganath and Chandrashila, with trail notes, season guidance, and preparation tips.",
      tags: ["Tunganath", "Chandrashila", "Trek", "Uttarakhand"],
      sections: [
        {
          heading: "Why Tunganath stands out",
          paragraphs: [
            "Tunganath is known as one of the highest Shiva temples and is often paired with the Chandrashila summit. The trail from Chopta is relatively short compared with many Himalayan treks, but the altitude and weather still require respect.",
            "The route is loved for forests, open ridgelines, temple atmosphere, and panoramic views when the sky is clear."
          ]
        },
        {
          heading: "Route and timing",
          paragraphs: [
            "Most travelers base around Chopta and trek up to Tunganath, continuing to Chandrashila if conditions and fitness allow. Winter can bring snow and a very different experience, while spring and autumn often provide clearer movement.",
            "Start early, carry layers, and check local conditions because snow, ice, and storms can alter the trail quickly."
          ]
        },
        {
          heading: "What to carry",
          paragraphs: [
            "Good shoes, warm clothing, water, snacks, sun protection, rain cover, and a small first-aid kit are sensible basics. The trail may feel accessible, but mountain weather does not negotiate.",
            "Travel light, walk steadily, and leave enough time to descend safely before dark."
          ]
        }
      ]
    },
    "rudranath-guide": {
      category: "Travel",
      date: "December 29, 2024",
      readTime: "6 min read",
      title: "Rudranath: A Hidden Gem in the Himalayas",
      sourceUrl: "https://workramanujan3.wordpress.com/2024/12/29/rudranath-a-hidden-gem-in-the-himalayas/",
      dek: "A guide to the remote Rudranath route, known for forests, meadows, long walking days, and a deeply quiet Himalayan setting.",
      tags: ["Rudranath", "Panch Kedar", "Trek", "Himalayas"],
      sections: [
        {
          heading: "The character of the trek",
          paragraphs: [
            "Rudranath is part of the Panch Kedar circuit and feels more remote than many popular routes. The trail can include forest paths, grasslands, steep climbs, and long distances between facilities.",
            "Its appeal is in the quiet. The landscape changes slowly, and the temple setting feels removed from the pace of ordinary travel."
          ]
        },
        {
          heading: "Preparation",
          paragraphs: [
            "Fitness matters because the route can involve sustained walking and elevation gain. Plan food, stay, water, and guide support carefully, especially outside peak movement periods.",
            "Weather and trail conditions should be checked locally before starting. A flexible itinerary is better than a tight one."
          ]
        },
        {
          heading: "Responsible travel",
          paragraphs: [
            "Rudranath's remoteness is part of its value, so low-impact travel is essential. Carry back waste, respect local settlements, and keep the route clean.",
            "For travelers who enjoy slower, quieter Himalayan journeys, Rudranath offers a rare mix of devotion, endurance, and solitude."
          ]
        }
      ]
    }
  };

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

  function showBlogList(updateHash = false) {
    if (!writingGrid || !blogReader) {
      return;
    }

    writingGrid.hidden = false;
    blogReader.hidden = true;

    if (updateHash && window.location.hash !== "#writing") {
      window.history.pushState(null, "", "#writing");
    }
  }

  function renderBlog(blogId, updateHash = true) {
    const article = blogArticles[blogId];
    if (!article || !writingGrid || !blogReader || !blogArticleContent || !blogSource) {
      return false;
    }

    const tags = article.tags.map((tag) => `<li>${tag}</li>`).join("");
    const sections = article.sections.map((section) => `
      <section class="blog-section">
        <h4>${section.heading}</h4>
        ${section.paragraphs.map((paragraph) => `<p>${paragraph}</p>`).join("")}
      </section>
    `).join("");

    blogArticleContent.innerHTML = `
      <header class="blog-article-head">
        <p>${article.category} - ${article.date} - ${article.readTime}</p>
        <h3>${article.title}</h3>
        <span>${article.dek}</span>
        <ul class="tag-list blog-tags">${tags}</ul>
      </header>
      <div class="blog-article-body">
        ${sections}
      </div>
    `;

    blogSource.href = article.sourceUrl;
    writingGrid.hidden = true;
    blogReader.hidden = false;

    if (updateHash && window.location.hash !== `#writing/${blogId}`) {
      window.history.pushState(null, "", `#writing/${blogId}`);
    }

    if (window.lucide) {
      window.lucide.createIcons();
    }

    blogReader.setAttribute("tabindex", "-1");
    blogReader.focus({ preventScroll: true });
    return true;
  }

  function activateTab(tabName, options = {}) {
    const preserveHash = Boolean(options.preserveHash);
    const resetWriting = Boolean(options.resetWriting);

    if (!preserveHash && window.location.hash !== `#${tabName}`) {
      window.history.replaceState(null, "", `#${tabName}`);
    }

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

    if (tabName !== "writing" || resetWriting) {
      showBlogList(false);
    }
  }

  function routeFromHash() {
    const hash = window.location.hash.replace("#", "");
    const [tabName, blogId] = hash.split("/");
    return { tabName, blogId };
  }

  function handleHashRoute(shouldScroll = false) {
    const { tabName, blogId } = routeFromHash();

    if (!tabName) {
      return;
    }

    if (!tabPanels.some((panel) => panel.dataset.panel === tabName)) {
      return;
    }

    activateTab(tabName, { preserveHash: true });

    if (tabName === "writing" && blogId) {
      if (!renderBlog(blogId, false)) {
        showBlogList(false);
      }
    } else if (tabName === "writing") {
      showBlogList(false);
    }

    if (shouldScroll) {
      scrollToWorkbench();
    }
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
      activateTab(button.dataset.tab, { resetWriting: true });
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

  blogLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      activateTab("writing", { preserveHash: true });
      renderBlog(link.dataset.blogId);
      closeMenu();
      scrollToWorkbench();
    });
  });

  if (blogBack) {
    blogBack.addEventListener("click", () => {
      showBlogList(true);
      scrollToWorkbench();
    });
  }

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

  handleHashRoute(false);

  window.addEventListener("popstate", () => {
    handleHashRoute(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
    }
  });

  const siteNav = document.querySelector(".site-nav");
  if (siteNav) {
    siteNav.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
        e.preventDefault();
        const activeIdx = tabButtons.findIndex(b => b.classList.contains("is-active"));
        let nextIdx = e.key === "ArrowRight" ? activeIdx + 1 : activeIdx - 1;
        if (nextIdx >= tabButtons.length) nextIdx = 0;
        if (nextIdx < 0) nextIdx = tabButtons.length - 1;
        
        const nextTab = tabButtons[nextIdx];
        activateTab(nextTab.dataset.tab, { resetWriting: true });
        nextTab.focus();
        scrollToWorkbench();
      }
    });
  }


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
    let lastScrollY = window.scrollY;
    
    window.addEventListener("scroll", () => {
      const currentScrollY = window.scrollY;
      
      if (currentScrollY < lastScrollY && currentScrollY > 400) {
        backToTopBtn.classList.add("is-visible");
      } else {
        backToTopBtn.classList.remove("is-visible");
      }
      
      lastScrollY = currentScrollY;
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

// Project Filtering Logic
const filterBtns = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    // Remove active class from all buttons
    filterBtns.forEach(b => b.classList.remove('active'));
    // Add active class to clicked button
    btn.classList.add('active');
    
    const filterValue = btn.getAttribute('data-filter');
    
    projectCards.forEach(card => {
      const categories = card.getAttribute('data-category') || '';
      if (filterValue === 'all' || categories.includes(filterValue)) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  });
});


  // Blog Filtering Logic
  const filterContainers = document.querySelectorAll('.blog-filters');
  filterContainers.forEach(container => {
    const listId = container.id.replace('filter-', 'list-');
    const list = document.getElementById(listId);
    if (!list) return;
    
    const items = list.querySelectorAll('.blog-item');
    const buttons = container.querySelectorAll('.tag-chip');
    
    buttons.forEach(button => {
      button.addEventListener('click', () => {
        buttons.forEach(b => b.classList.remove('active'));
        button.classList.add('active');
        
        const filter = button.getAttribute('data-tag');
        
        items.forEach(item => {
          if (filter === 'all') {
            item.classList.remove('hidden');
          } else {
            const tags = item.getAttribute('data-tags').split(' ');
            if (tags.includes(filter)) {
              item.classList.remove('hidden');
            } else {
              item.classList.add('hidden');
            }
          }
        });
      });
    });
  });
