// AUTO_QFIT.h : main header file for the AUTO_QFIT application
//

#if !defined(AFX_AUTO_QFIT_H__E7C44347_A66A_4D3A_B56F_23765CA84C43__INCLUDED_)
#define AFX_AUTO_QFIT_H__E7C44347_A66A_4D3A_B56F_23765CA84C43__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CAUTO_QFITApp:
// See AUTO_QFIT.cpp for the implementation of this class
//

class CAUTO_QFITApp : public CWinApp
{
public:
	CAUTO_QFITApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAUTO_QFITApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CAUTO_QFITApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_AUTO_QFIT_H__E7C44347_A66A_4D3A_B56F_23765CA84C43__INCLUDED_)
