﻿namespace MyWin06
{
    partial class Form1
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblFirst = new System.Windows.Forms.Label();
            this.lblLast = new System.Windows.Forms.Label();
            this.tbFirst = new System.Windows.Forms.TextBox();
            this.tbLast = new System.Windows.Forms.TextBox();
            this.btn = new System.Windows.Forms.Button();
            this.tbml = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // lblFirst
            // 
            this.lblFirst.AutoSize = true;
            this.lblFirst.Location = new System.Drawing.Point(58, 49);
            this.lblFirst.Name = "lblFirst";
            this.lblFirst.Size = new System.Drawing.Size(49, 12);
            this.lblFirst.TabIndex = 0;
            this.lblFirst.Text = "첫별수 :";
            // 
            // lblLast
            // 
            this.lblLast.AutoSize = true;
            this.lblLast.Location = new System.Drawing.Point(58, 91);
            this.lblLast.Name = "lblLast";
            this.lblLast.Size = new System.Drawing.Size(49, 12);
            this.lblLast.TabIndex = 1;
            this.lblLast.Text = "끝별수 :";
            // 
            // tbFirst
            // 
            this.tbFirst.Location = new System.Drawing.Point(154, 43);
            this.tbFirst.Name = "tbFirst";
            this.tbFirst.Size = new System.Drawing.Size(100, 21);
            this.tbFirst.TabIndex = 2;
            // 
            // tbLast
            // 
            this.tbLast.Location = new System.Drawing.Point(154, 88);
            this.tbLast.Name = "tbLast";
            this.tbLast.Size = new System.Drawing.Size(100, 21);
            this.tbLast.TabIndex = 3;
            // 
            // btn
            // 
            this.btn.Location = new System.Drawing.Point(65, 132);
            this.btn.Name = "btn";
            this.btn.Size = new System.Drawing.Size(189, 23);
            this.btn.TabIndex = 4;
            this.btn.Text = "별그리기";
            this.btn.UseVisualStyleBackColor = true;
            this.btn.Click += new System.EventHandler(this.btn_Click);
            // 
            // tbml
            // 
            this.tbml.Location = new System.Drawing.Point(65, 173);
            this.tbml.Multiline = true;
            this.tbml.Name = "tbml";
            this.tbml.Size = new System.Drawing.Size(189, 172);
            this.tbml.TabIndex = 5;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(329, 388);
            this.Controls.Add(this.tbml);
            this.Controls.Add(this.btn);
            this.Controls.Add(this.tbLast);
            this.Controls.Add(this.tbFirst);
            this.Controls.Add(this.lblLast);
            this.Controls.Add(this.lblFirst);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblFirst;
        private System.Windows.Forms.Label lblLast;
        private System.Windows.Forms.TextBox tbFirst;
        private System.Windows.Forms.TextBox tbLast;
        private System.Windows.Forms.Button btn;
        private System.Windows.Forms.TextBox tbml;
    }
}

