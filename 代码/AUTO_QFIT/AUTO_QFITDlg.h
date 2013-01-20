// AUTO_QFITDlg.h : header file
//

#if !defined(AFX_AUTO_QFITDLG_H__DE8D0617_80C6_4683_A297_F707BA08E03E__INCLUDED_)
#define AFX_AUTO_QFITDLG_H__DE8D0617_80C6_4683_A297_F707BA08E03E__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CAUTO_QFITDlg dialog

class CAUTO_QFITDlg : public CDialog
{
// Construction
public:
	CAUTO_QFITDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	//{{AFX_DATA(CAUTO_QFITDlg)
	enum { IDD = IDD_AUTO_QFIT_DIALOG };
		// NOTE: the ClassWizard will add data members here
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAUTO_QFITDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL
	CString m_MBMDir;
// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	//{{AFX_MSG(CAUTO_QFITDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnStart();
	afx_msg void OnBrowser();
	afx_msg void OnChangeDir();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_AUTO_QFITDLG_H__DE8D0617_80C6_4683_A297_F707BA08E03E__INCLUDED_)
