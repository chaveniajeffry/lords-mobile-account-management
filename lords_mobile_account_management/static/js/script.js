// Get all elements with IDs matching the pattern "content-{number}"
const elements = document.querySelectorAll("[id^='lmContent']");

// Loop through each element and extract the number from the ID
elements.forEach(element => {
  const id = element.id;
  const number = parseInt(id.replace("lmContent", ""));
  // Apply grid layout with dynamically calculated number of template columns
  element.style.display = "grid";
  element.style.gridTemplateColumns = `repeat(${number}, 1fr)`;
  element.style.gridTemplateRows = "1fr 1fr";
  element.style.gap = "10px 10px";
  // You can adjust the number or use different logic to determine columns
});