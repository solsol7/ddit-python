using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyWin05
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btn_Click(object sender, EventArgs e)
        {
            Random rndObj = new Random();
            int rnd = rndObj.Next(3);
            String com = "";
            String result = "";

            if(rnd == 0) { com = "가위"; }
            else if(rnd == 1) { com = "바위"; }
            else if(rnd == 2) { com = "보"; }

            String Mine = tbMine.Text;

            if(Mine=="가위"&&com=="바위" || Mine == "바위" && com == "보" || Mine == "보" && com == "가위")
            {
                result = "짐";
            }else if(Mine == "바위" && com == "바위" || Mine == "보" && com == "보" || Mine == "가위" && com == "가위")
            {
                result = "비김";
            }
            else
            {
                result = "이김";
            }
            tbCom.Text = com;
            tbResult.Text = result;

        }
    }
}
