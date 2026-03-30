<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Upload.aspx.cs" Inherits="Upload" %>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Assessment Submission</title>
<style>
    /* Reset & base styling */
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }

    body {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background: linear-gradient(135deg, #74ebd5, #ACB6E5);
    }

    .container {
        background: #fff;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
        width: 100%;
        max-width: 500px;
        text-align: center;
    }

    h2 {
        margin-bottom: 20px;
        color: #4a4a4a;
        font-size: 28px;
    }

    .instructions {
        background: #f0f8ff;
        padding: 15px 20px;
        border-left: 5px solid #36d1dc;
        border-radius: 8px;
        text-align: left;
        font-size: 14px;
        margin-bottom: 25px;
        color: #333;
    }

    .instructions ul {
        list-style-type: disc;
        margin-left: 20px;
    }

    .file-upload {
        margin: 20px 0;
        display: flex;
        justify-content: center;
    }

    input[type="file"] {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 10px;
        cursor: pointer;
        transition: 0.3s;
    }

    input[type="file"]:hover {
        border-color: #4ecdc4;
    }

    .btn {
        display: inline-block;
        padding: 12px 25px;
        margin: 10px 5px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        transition: 0.3s;
        border: none;
        color: #fff;
    }

    .btn-upload {
        background: linear-gradient(90deg, #36d1dc, #5b86e5);
    }

    .btn-upload:hover {
        background: linear-gradient(90deg, #5b86e5, #36d1dc);
    }

    .btn-back {
        background: linear-gradient(90deg, #f66a6a, #ff4b4b);
    }

    .btn-back:hover {
        background: linear-gradient(90deg, #ff4b4b, #f66a6a);
    }

    #status {
        margin-top: 20px;
        font-weight: 500;
        min-height: 24px;
        color: #333;
    }

    /* Responsive */
    @media (max-width: 500px) {
        .container {
            padding: 30px 20px;
        }
        h2 { font-size: 24px; }
    }
</style>
</head>
<body>

<div class="container">
    <h2>Upload Your File</h2>

    <!-- Instructions Section -->
    <div class="instructions">
        <strong>Important Instructions:</strong>
        <ul>
            <li>Make sure your file is named correctly according to the guidelines.</li>
            <li>Double-check your file format is supported.</li>
            <li>Ensure the file size is within the allowed limit.</li>
            <li>Verify any related dependencies or files are included if required.</li>
        </ul>
    </div>

    <form id="uploadForm" runat="server" enctype="multipart/form-data">
        <div class="file-upload">
            <asp:FileUpload ID="fileInput" runat="server" CssClass="file-input" />
        </div>
        <div>
            <asp:Button ID="btnUpload" runat="server" Text="Upload" CssClass="btn btn-upload" OnClick="UploadFile_Click" />
            <button type="button" class="btn btn-back" onclick="history.back()">Back</button>
        </div>
    </form>

    <div id="status">
        <asp:Label ID="lblStatus" runat="server" />
    </div>
</div>

</body>
</html>