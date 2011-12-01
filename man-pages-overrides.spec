Summary: Complementary and updated manual pages
Name: man-pages-overrides
Version: 1.0
Release: 1%{?dist}
# man - GPLv2
License: GPLv2
Group: Documentation
# there is no public download location for this package
Source0: man-pages-overrides-%{version}.tar.gz
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires: man >= 1.6f-24

%description
A collection of manual ("man") pages to complement other packages or update
those contained therein. Always have the latest version of this package
installed.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/overrides
mkdir -p $RPM_BUILD_ROOT%{_docdir}
for i in `ls`; do
    if [ -d $i ]
    then
        for j in `ls $i`; do
           if [ -d $i/$j ]
           then
               mkdir -p $RPM_BUILD_ROOT%{_mandir}/overrides/$j
               cp -f $i/$j/* $RPM_BUILD_ROOT%{_mandir}/overrides/$j
           else
              mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$i
              cp $i/$j $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$i
           fi
        done
    fi
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/overrides

%changelog
* Mon Oct 19 2009 Ivana Varekova <varekova@redhat.com> 1.0-1
- made a initial package
