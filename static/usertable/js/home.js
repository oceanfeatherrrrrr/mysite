document.getElementById('logout-link').addEventListener('click', function(e) {
    e.preventDefault(); // 阻止默认的链接行为

    // 发送一个POST请求到服务器上的登出API
    fetch('/api/logout/', {
        method: 'POST', // 使用POST方法发送请求
        credentials: 'include', // 如果你的Django应用启用了CSRF保护，并且你想要包含cookies（如session cookie），则添加此行
        headers: {
            'Content-Type': 'application/json', // 如果你需要发送JSON数据，但在这个例子中我们不需要
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('注销失败: ' + response.statusText);
        }
        return response.json(); // 解析JSON响应
    })
    .then(data => {
        // 处理从服务器返回的数据
        alert(data.message); // 显示登出成功的消息
        // 在这里可以添加重定向到登录页面或其他页面的逻辑
        // window.location.href = '/login';
    })
    .catch(error => {
        console.error('注销时发生错误:', error);
        alert('注销失败，请重试。');
    });
});