using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyWin03
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btn_Click(object sender, EventArgs e)
        {
            int dan = Int32.Parse(tbDan.Text);
            String printDan = "";

            for (int i = 1; i <= 9; i++)
            {
                /* printDan += dan + "*" + i + "=" + dan * i +"\r\n";*/
                printDan += string.Format("{0}*{1}={2}\r\n", dan, i, dan * i);
            }

            tbPrint.Text = printDan;

        }
    }
}
