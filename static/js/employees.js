document.addEventListener("click", function (e) {

    // page-link를 클릭한 경우에만 실행
    const link = e.target.closest("a.page-link");
    if (!link) return;

    // 이전/다음 비활성(span) 제외
    if (!link.getAttribute("href")) return;

    // 기본 이벤트 실행을 막음
    e.preventDefault();

    // html의 page-link에서 이미 만들어 둔 url 가져오기
    const url = link.getAttribute("href"); // ?page=2

    // 비동기 요청 ( .then : 성공 시 처리, .catch : 실패 시 처리 )
    fetch(url, {
        headers: { "X-Requested-With": "fetch" }
    }) 
    .then(res => {
        // HTTP 오류(404, 500)는 fetch 자체 에러가 아니라서 이게 없으면 처리 못함. 
        if (!res.ok) {
            throw new Error(`HTTP error: ${res.status}`);
        }
        // 정상적으로 응답을 받고, fetch도 성공한 경우에 http응답 본문을 text로 읽어라.
        return res.text();
    })
    .then(html => {
        console.log("html : ",html)
        // text로 읽은 본문에서 table부분 ()
        const doc = new DOMParser().parseFromString(html, "text/html");
        document.querySelector("#employees-table").innerHTML =
            doc.querySelector("#employees-table").innerHTML;
    })
    .catch(err => {
        console.error(err);
        alert("데이터 갱신 중 오류 발생");
    });

});