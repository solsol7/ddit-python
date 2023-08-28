using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyWin04
{
    public partial class Form1 : Form
    {
        String number = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void btn_Click(object sender, EventArgs e)
        {
            number += ((Button)sender).Text;
            tb.Text = number;
        }

        private void callBtn_Click(object sender, EventArgs e)
        {
            MessageBox.Show(number+"\ncalling");
        }

        private void remove_Click(object sender, EventArgs e)
        {
            number = number.Substring(0,number.Length - 1);
            tb.Text = number;
        }
    }
}
