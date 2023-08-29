using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyWin06
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public String getStar(int cnt)
        {
            String ret = "";
            for(int i = 0; i < cnt; i++) {
                ret += "*";
            }
            ret += "\r\n";

            return ret;
        }

        private void btn_Click(object sender, EventArgs e)
        {

            int first = Int32.Parse(tbFirst.Text);
            int last = Int32.Parse(tbLast.Text);
            String text = "";

            for (int i = first; i <= last; i++)
            {
               text += getStar(i);
            }
            tbml.Text = text;
        }

        /*
        private void btn_Click(object sender, EventArgs e)
        {

            int first = Int32.Parse(tbFirst.Text);
            int last = Int32.Parse(tbLast.Text);
            int total = last - first;
            tbml.Text = "";

            for (int i = 0; i <= total; i++)
            {
                for(int j=0; j<first; j++)
                {
                    tbml.Text += "*";
                }
                first += 1;
                tbml.Text += "\r\n";
            }
        }

        */
    }
}
