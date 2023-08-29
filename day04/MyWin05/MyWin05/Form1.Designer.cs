namespace MyWin05
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
            this.lblMine = new System.Windows.Forms.Label();
            this.lblCom = new System.Windows.Forms.Label();
            this.lblResult = new System.Windows.Forms.Label();
            this.tbMine = new System.Windows.Forms.TextBox();
            this.tbCom = new System.Windows.Forms.TextBox();
            this.tbResult = new System.Windows.Forms.TextBox();
            this.btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblMine
            // 
            this.lblMine.AutoSize = true;
            this.lblMine.Location = new System.Drawing.Point(74, 51);
            this.lblMine.Name = "lblMine";
            this.lblMine.Size = new System.Drawing.Size(29, 12);
            this.lblMine.TabIndex = 0;
            this.lblMine.Text = "나 : ";
            // 
            // lblCom
            // 
            this.lblCom.AutoSize = true;
            this.lblCom.Location = new System.Drawing.Point(74, 88);
            this.lblCom.Name = "lblCom";
            this.lblCom.Size = new System.Drawing.Size(17, 12);
            this.lblCom.TabIndex = 1;
            this.lblCom.Text = "컴";
            // 
            // lblResult
            // 
            this.lblResult.AutoSize = true;
            this.lblResult.Location = new System.Drawing.Point(74, 129);
            this.lblResult.Name = "lblResult";
            this.lblResult.Size = new System.Drawing.Size(41, 12);
            this.lblResult.TabIndex = 2;
            this.lblResult.Text = "결과 : ";
            // 
            // tbMine
            // 
            this.tbMine.Location = new System.Drawing.Point(109, 48);
            this.tbMine.Name = "tbMine";
            this.tbMine.Size = new System.Drawing.Size(100, 21);
            this.tbMine.TabIndex = 3;
            // 
            // tbCom
            // 
            this.tbCom.Location = new System.Drawing.Point(109, 85);
            this.tbCom.Name = "tbCom";
            this.tbCom.Size = new System.Drawing.Size(100, 21);
            this.tbCom.TabIndex = 4;
            // 
            // tbResult
            // 
            this.tbResult.Location = new System.Drawing.Point(109, 126);
            this.tbResult.Name = "tbResult";
            this.tbResult.Size = new System.Drawing.Size(100, 21);
            this.tbResult.TabIndex = 5;
            // 
            // btn
            // 
            this.btn.Location = new System.Drawing.Point(109, 175);
            this.btn.Name = "btn";
            this.btn.Size = new System.Drawing.Size(75, 23);
            this.btn.TabIndex = 6;
            this.btn.Text = "게임하기";
            this.btn.UseVisualStyleBackColor = true;
            this.btn.Click += new System.EventHandler(this.btn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(300, 285);
            this.Controls.Add(this.btn);
            this.Controls.Add(this.tbResult);
            this.Controls.Add(this.tbCom);
            this.Controls.Add(this.tbMine);
            this.Controls.Add(this.lblResult);
            this.Controls.Add(this.lblCom);
            this.Controls.Add(this.lblMine);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblMine;
        private System.Windows.Forms.Label lblCom;
        private System.Windows.Forms.Label lblResult;
        private System.Windows.Forms.TextBox tbMine;
        private System.Windows.Forms.TextBox tbCom;
        private System.Windows.Forms.TextBox tbResult;
        private System.Windows.Forms.Button btn;
    }
}

