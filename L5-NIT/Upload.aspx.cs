using System;
using System.IO;

public partial class Upload : System.Web.UI.Page
{
    protected void UploadFile_Click(object sender, EventArgs e)
    {
        if (fileInput.HasFile)
        {
            try
            {
                string folderPath = Server.MapPath("~/uploads/");
                
                // Ensure the folder exists
                if (!Directory.Exists(folderPath))
                    Directory.CreateDirectory(folderPath);

                string filePath = Path.Combine(folderPath, fileInput.FileName);

                // Check if file already exists
                if (File.Exists(filePath))
                {
                    lblStatus.Text = "A file with this name already exists. Please rename your file and try again.";
                    return;
                }

                // Save the uploaded file
                fileInput.SaveAs(filePath);
                lblStatus.Text = "File uploaded successfully: " + fileInput.FileName;
            }
            catch (Exception ex)
            {
                lblStatus.Text = "Upload failed: " + ex.Message;
            }
        }
        else
        {
            lblStatus.Text = "Please select a file first.";
        }
    }
}