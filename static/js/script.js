
// Search functionality
console.log('Hello.... ')

document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.getElementById("search-form");
  const searchInput = document.getElementById("search-input");
  const searchButton = document.getElementById("search-button");

try{
  searchForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const query = searchInput.value.trim();
    if (query) {
      // Redirect to search page with query parameter
      window.location.href = `/search?query=${encodeURIComponent(query)}`;
    } else {
      alert("Please enter a search term");
    }
  });
}
catch(e){

}

try{
  searchButton.addEventListener("click", function () {
    searchForm.submit();
  });
}
catch(e){

}

});


// Voice and others search functionality

// document.addEventListener("DOMContentLoaded", function () {
  
  const voiceSearchBtn = document.getElementsByClassName('voice-search-btn');
  console.log("Mobile search")
  const searchQueryInput = document.getElementById('search-query-full');
  const searchQueryInputMobile = document.getElementById('search-query-mobile');
  const searchForm = searchQueryInput.closest('form');  // Get the form element
  const voiceSearchPopup = document.getElementsByClassName('voice-search-popup');  // Get the popup element
  console.log(voiceSearchBtn)
  // Check if the browser supports speech recognition
  if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
    
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';  // Set language

    for (element of voiceSearchBtn){
      console.log(element)
      element.addEventListener('click', function (event) {
        console.log('Print voice search something')
        event.preventDefault();  // Prevent form submission when clicking mic button
        for (popup of voiceSearchPopup){
          popup.classList.remove("hidden");  // Show the popup
          popup.classList.add("flex", "items-center", "justify-center")
        }
        recognition.start();  // Start listening to voice
  
      });
    }
    

    recognition.onresult = function (event) {
      let speechResult = event.results[0][0].transcript;  // Get the recognized text
      // Capitalize the first letter
      speechResult = speechResult.charAt(0).toUpperCase() + speechResult.slice(1);
      console.log(speechResult)
      searchQueryInput.value = speechResult;  // Put the result into the input field
      searchQueryInputMobile.value = speechResult;

      // Hide the popup after voice input is done
      for (popup of voiceSearchPopup){
      popup.classList.add('hidden');
      popup.classList.remove("flex");
      popup.classList.remove("items-center");
      popup.classList.remove("justify-center");
      }
      // Add a 2-second delay before submitting the form
      setTimeout(function() {
        searchForm.submit();  // Automatically submit the form
      }, 2000);  // 2000 milliseconds = 2 seconds
    };

    recognition.onspeechend = function () {
      recognition.stop();  // Stop recognition when speech ends
      for (popup of voiceSearchPopup){
      popup.classList.add('hidden');  // Hide the popup
      }
    };

    recognition.onerror = function (event) {
      console.error('Speech recognition error: ' + event.error);
      for (popup of voiceSearchPopup){
      popup.classList.add('hidden');  // Hide the popup if there's an error
      }
    };
  } else {
    console.warn('Speech recognition not supported in this browser.');
    for (btn of voiceSearchBtn){
    btn.disabled = true;  // Disable the mic button if not supported
    
  }
}