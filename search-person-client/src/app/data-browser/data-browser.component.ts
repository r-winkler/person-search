import { Component, OnInit, ViewChild } from '@angular/core';
import { UntypedFormControl } from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';
import { SucheService } from '../suche/suche.service';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { debounceTime } from 'rxjs/operators';
import { PersonDTO } from '../person.dto';

@Component({
    selector: 'app-data-browser',
    templateUrl: './data-browser.component.html',
    styleUrls: ['./data-browser.component.scss']
})
export class DataBrowserComponent implements OnInit {

    displayedColumns: string[] = ['name', 'firstname'];
    dataSource = new MatTableDataSource();
    filterFormControl = new UntypedFormControl();

    // @ts-ignore
    @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
    // @ts-ignore
    @ViewChild('tableSort', { static: true }) tableSort: MatSort;

    constructor(private sucheService: SucheService) {
    }

    ngOnInit(): void {

        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.tableSort;
        this.sucheService.findAll().subscribe(data => this.dataSource.data = data);
        this.setFilterPredicate();
        this.filterFormControl.valueChanges.pipe(debounceTime(500)).subscribe(() => this.applyFilter());
    }



    private setFilterPredicate(): void {

        // @ts-ignore
        this.dataSource.filterPredicate = (data: PersonDTO, filter) => {
            const dataStr = (data.name + data.firstname).toLowerCase();

            let dataContainsFilter = true;
            filter.split(' ').forEach(filterItem => {
                if (filterItem !== '' && dataContainsFilter) {
                    dataContainsFilter = dataStr.indexOf(filterItem) !== -1;
                }
            });
            return dataContainsFilter;
        };
    }


    private applyFilter(): void {

        this.dataSource.filter = this.filterFormControl.value != null ? this.filterFormControl.value.trim().toLowerCase() : null;
        // @ts-ignore
        this.dataSource.paginator.firstPage();
    }

}
