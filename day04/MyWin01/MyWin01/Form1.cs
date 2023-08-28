using System.Diagnostics;

namespace MyWin01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btn_Click(object sender, EventArgs e)
        {
           Console.Write(lbl.Text);
            if (lbl.Text=="Good Morning")
            {
                lbl.Text = "Good Evening";
            }
            else
            {
                lbl.Text = "Good Morning";
            }
            
        }
    }
}