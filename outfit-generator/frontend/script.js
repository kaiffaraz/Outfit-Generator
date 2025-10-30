document.getElementById("generateBtn").addEventListener("click", async () => {
  const shirts = document.getElementById("shirts").files;
  const pants = document.getElementById("pants").files;
  const status = document.getElementById("status");
  const gallery = document.getElementById("outfitGallery");

  if (shirts.length === 0 || pants.length === 0) {
    status.innerText = "⚠️ Please upload both shirts and pants!";
    return;
  }

  status.innerText = "⏳ Generating outfit combinations...";
  gallery.innerHTML = "";

  const formData = new FormData();
  for (let s of shirts) formData.append("shirts", s);
  for (let p of pants) formData.append("pants", p);

  try {
    const response = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    if (data.error) {
      status.innerText = `❌ ${data.error}`;
      return;
    }

    status.innerText = "✅ Outfit combinations generated! Click to preview.";

    const dummyModel = document.getElementById("dummyModel");

    data.outfits.forEach((outfit, index) => {
      const card = document.createElement("div");
      card.className = "outfit-card";
      card.innerHTML = `
        <img src="${outfit.shirt}" alt="Shirt">
        <img src="${outfit.pant}" alt="Pant">
        <div class="outfit-name">👕 ${outfit.name}</div>
        <div class="combo-text">Stylish combo: White shirt + Black pant</div>
      `;

      // On click, change mannequin outfit color
      card.addEventListener("click", () => {
        applyOutfitToModel(outfit, dummyModel);
      });

      gallery.appendChild(card);
    });
  } catch (err) {
    status.innerText = "❌ Error generating outfits. Check console.";
    console.error(err);
  }
});

/**
 * Apply shirt/pant colors to 3D mannequin model
 */
function applyOutfitToModel(outfit, dummyModel) {
  if (!dummyModel) return;

  // Simulate shirt/pant colors using environment tint filters
  dummyModel.style.filter = `contrast(1.2) brightness(1.1) saturate(1.2) drop-shadow(0 0 20px ${outfit.shirtColor})`;
  dummyModel.style.background = `linear-gradient(to bottom, ${outfit.shirtColor} 40%, ${outfit.pantColor} 60%)`;

  // Smooth transition effect
  dummyModel.animate([
    { transform: "scale(1) rotateY(0deg)" },
    { transform: "scale(1.05) rotateY(360deg)" },
    { transform: "scale(1) rotateY(0deg)" }
  ], {
    duration: 2000,
    iterations: 1
  });
}
