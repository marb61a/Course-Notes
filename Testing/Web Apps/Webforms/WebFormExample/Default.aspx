<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="WebFormAppScenarioEx.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>WebForm Example</title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            Enter Name : <asp:textbox ID="NameTextBox" runat="server"/>
        </div>
        <div>
            Enter Email : <asp:textbox ID="EmailTextbox" runat="server"/>
        </div>
        <div>
            <asp:Button ID="SubscribeButton" runat="server" Text="Subscribe" OnClick="SubscribeButton_Click"/>
        </div>
    </form>
</body>
</html>
