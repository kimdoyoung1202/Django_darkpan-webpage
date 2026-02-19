function fetch_live() {

    // 서버에 GET 요청을 비동기로 보냄
    fetch('/departments/fetch-live')
        .then(response => response.json())    // 응답을 받음.(응답 본문을 json으로 파싱)
        .then(data => { console.log(data) })    // 응답 내용을 출력 (정상)
        .catch(error => { console.log(error) }) // 응답 내용을 출력 (오류)
        ;
}


function fetch_sleep() {

    // 서버에 GET 요청을 비동기로 보냄
    fetch('/departments/fetch-sleep')
        .then(response => response.json())    // 응답을 받음.(응답 본문을 json으로 파싱)
        .then(data => { console.log(data) })    // 응답 내용을 출력 (정상)
        .catch(error => { console.log(error) }) // 응답 내용을 출력 (오류)
        ;
}

function get_cookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}



// 모달 창의 추가 버튼에 클릭 이벤트 핸들러 등록
// 비동기 통신을 하기 위해
document.getElementById("dept_save").addEventListener("click", function (e) {

    // 기본 동작 막음
    e.preventDefault();

    // 버튼 중복 클릭 방지
    const btn = this;
    btn.disabled = true;

    // 폼 입력 데이터 가져오기
    const form = document.getElementById("dept_add_form");
    const form_data = new FormData(form);
    const url = form.action;

    // 비동기로 POST 요청
    fetch(url, {
        method: "POST",
        headers: {
            "X-CSRFToken": get_cookie("csrftoken"), //없으면 장고에서 요청 안받음
            "X-Requested-With": "fetch"
        },
        body: form_data
    })
        .then(res => {
            if (!res.ok) {
                // 403/400/500 등
                throw new Error("HTTP error: " + res.status);
            }
            return res.json();
        })
        .then(data => {
            // 서버에서 {dept_no: "d100", dept_name: "개발팀"} 반환
            const tbody = document.getElementById("dept_body");

            // 새로 추가된 부서를 표시할 행 생성
            const tr = document.createElement("tr");
            tr.setAttribute("data-dept-no", data.dept_no);

            tr.innerHTML = makeInnerHTML(data);

            // 최신이 위로 오게 하고 싶으면 prepend, 아래로 쌓이면 append
            tbody.prepend(tr);

            // 모달 닫기 (Bootstrap 5)
            const modalEl = document.getElementById("dept_add_modal");
            const modal = bootstrap.Modal.getInstance(modalEl);
            modal.hide();
        })
        .catch(err => {
            alert(err.message);
            console.log(err.message);
        })
        .finally(() => {
            btn.disabled = false;
        });

});


function makeInnerHTML(dept) {



    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || '';

    return `
    <th scope="row">
    <a href="/departments/${dept.dept_no}/update/">
        ${dept.dept_no}
    </a>
    </th>

    <td>${dept.dept_name}</td>

    <td>
    <form method="post"
            action="/departments/delete/${dept.dept_no}"
            onsubmit="return confirm('정말 삭제 하시겠습니까?');">

        <input type="hidden"
            name="csrfmiddlewaretoken"
            value="${csrfToken}">

        <button type="submit"
                class="btn btn-sm btn-outline-danger">
        삭제
        </button>
    </form>
    </td>

    <td>
    <button class="btn btn-success rounded-pill m-2"
            onclick="fetch_live()">
        비동기
    </button>
    </td>`;
}