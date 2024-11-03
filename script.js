// Telegram Web App SDK ব্যবহার করে bot-এ তথ্য পাঠানো
function sendMessage() {
    const tg = window.Telegram.WebApp; // Telegram WebApp SDK ব্যবহার করা
    tg.sendData("Hello from PixelChaser!"); // bot-এ তথ্য পাঠানো
    alert("Message sent to bot!"); // ব্যবহারকারীকে নিশ্চিতকরণ বার্তা
}

// Web App এর থিম সেটআপ করা
window.Telegram.WebApp.onEvent('themeChanged', function() {
    document.body.style.backgroundColor = window.Telegram.WebApp.themeParams.bg_color;
});
