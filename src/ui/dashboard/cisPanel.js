export function renderCisPanel(data) {
    const el = document.getElementById("cis-panel");
    if (!el) return;
    if (!Array.isArray(data)) {
        el.innerHTML = "<em>No CIS data available</em>"; 
      return;
    }

    el.innerHTML = data
        .map(c => `
          <div class="cis-item">
            <div class="cis-control">${c.control || ''}</div>
            <div class="cis-ig">
              <span><b>IG1:</b> ${c.IG1 || ''}</span>
              <span><b>IG2:</b> ${c.IG2 || ''}</span>
              <span><b>IG3:</b> ${c.IG3 || ''}</span>
            </div>
          </div>
        `)
      .join("");
  }
  
