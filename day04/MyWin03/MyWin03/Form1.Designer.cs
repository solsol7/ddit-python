namespace MyWin03
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
            this.tbPrint = new System.Windows.Forms.TextBox();
            this.btn = new System.Windows.Forms.Button();
            this.lbl = new System.Windows.Forms.Label();
            this.tbDan = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // tbPrint
            // 
            this.tbPrint.Location = new System.Drawing.Point(61, 123);
            this.tbPrint.Multiline = true;
            this.tbPrint.Name = "tbPrint";
            this.tbPrint.Size = new System.Drawing.Size(199, 215);
            this.tbPrint.TabIndex = 0;
            // 
            // btn
            // 
            this.btn.Location = new System.Drawing.Point(61, 77);
            this.btn.Name = "btn";
            this.btn.Size = new System.Drawing.Size(75, 23);
            this.btn.TabIndex = 1;
            this.btn.Text = "출력하기";
            this.btn.UseVisualStyleBackColor = true;
            this.btn.Click += new System.EventHandler(this.btn_Click);
            // 
            // lbl
            // 
            this.lbl.AutoSize = true;
            this.lbl.Location = new System.Drawing.Point(59, 48);
            this.lbl.Name = "lbl";
            this.lbl.Size = new System.Drawing.Size(53, 12);
            this.lbl.TabIndex = 2;
            this.lbl.Text = "출력단수";
            // 
            // tbDan
            // 
            this.tbDan.Location = new System.Drawing.Point(160, 39);
            this.tbDan.Name = "tbDan";
            this.tbDan.Size = new System.Drawing.Size(100, 21);
            this.tbDan.TabIndex = 3;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(325, 364);
            this.Controls.Add(this.tbDan);
            this.Controls.Add(this.lbl);
            this.Controls.Add(this.btn);
            this.Controls.Add(this.tbPrint);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbPrint;
        private System.Windows.Forms.Button btn;
        private System.Windows.Forms.Label lbl;
        private System.Windows.Forms.TextBox tbDan;
    }
}

