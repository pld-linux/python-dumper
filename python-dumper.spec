
%include	/usr/lib/rpm/macros.python
%define 	module	dumper

Summary:	Python module for dumping nested data structures
Summary(pl):	Modu³ Pythona umo¿liwiaj±cy wypisywanie zawarto¶ci z³o¿onych struktur danych
Name:		python-%{module}
Version:	1.0
Release:	1
License:	CNRI
Group:		Libraries/Python
Source0:	http://www.mems-exchange.org/software/files/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	be7c0681c1819b244fd43c01ba6b9f67
URL:		http://www.mems-exchange.org/software/dumper/
BuildRequires:	python-devel >= 1.5
Requires:	python >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dumper is a module that provides tools for dumping deeply nested
Python data in a readable, customizable, controllable way. It handles
recursive structures, class instances, and lets you control how deeply
the dump goes in a couple of ways.

%description -l pl
dumper jest modu³em umo¿liwiaj±cym wy¶wietlanie zawarto¶ci z³o¿onych i
zagnie¿d¿onych struktur Pythona w czytelny, konfigurowalny i
sterowalny sposób. Obs³uguje rekurencyjne struktury danych, instancje
klas oraz pozwala na kontrolê g³êboko¶ci analizy przetwarzanych
obiektów.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/dumper.py[oc]
