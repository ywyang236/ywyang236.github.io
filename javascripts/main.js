// ######### 自我介紹 #########

// 取得畫面上需要操作的DOM
// 語法糖
const introForm = document.getElementById("introForm"),
    introBtn = document.getElementById("introBtn"),
    introName = document.getElementById("introName"),
    introOutput = document.getElementById("introOutput");

// 綁定表單的送出事件
introForm.addEventListener("submit", function (e) {
    // 預防表單重整畫面的預設行為
    e.preventDefault();
    // 表單送出後要做的事...
    // 取得輸入框的 value
    const name = introName.value,
        // 產生一段自我介紹的字串
        intro = `
        <div class="alert alert-warning mt-3" style="text-align:justify"><p>
        WeHelp 的 ${name} 您好 👋，<br><br>我是楊于葳，2018年於亞洲大學生物科技學系畢業，之後以企業二代的身份，進入製造業的家族公司上班，工作內容主要是技術開發與業務開發。期間，獨自以 Dreamwaver 設計公司網站，成功吸引國內、國外的客戶訂單後，開始對程式設計感到濃厚的興趣，決定到台大資訊系統訓練班學習。<br><br>
        公司因疫情歇業，因此目前正以成為前端工程師為轉職目標，全職學習資工領域的相關知識，希望能用最短的時間，成為獨立作業的前端工程師。
        </p></div>`;
    // 將自我介紹作為 introOutput 的文字內容
    introOutput.innerHTML = intro;
});



// #########  圖片下拉選擇器 #########

const imageSelector = document.getElementById("imageSelector");
imageSelector.addEventListener("change", function () {
    // 取得選擇的圖片
    const image = imageSelector.value;
    // 將圖片顯示到指定的標籤上
    document.getElementById("imagePreview").setAttribute("src", `./images/${image}.jpeg`);
});



// ######### 圖片左右選擇器＋文字 #########
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
    showDivs(slideIndex += n);
}

function showDivs(n) {
    var i;
    var x = document.getElementsByClassName("mySlides");
    if (n > x.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = x.length }
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[slideIndex - 1].style.display = "block";
}


// ######### 進度條 #########

function move() {
    var elem = document.getElementById("myBar");
    var width = 20;
    var id = setInterval(frame, 10);
    function frame() {
        if (width >= 100) {
            clearInterval(id);
        } else {
            width++;
            elem.style.width = width + '%';
            elem.innerHTML = width * 1 + '%';
        }
    }
}

// ######### 自動播放器 #########
var myIndex = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("mySlides2");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    myIndex++;
    if (myIndex > x.length) { myIndex = 1 }
    x[myIndex - 1].style.display = "block";
    setTimeout(carousel, 2000); // Change image every 2 seconds
}
