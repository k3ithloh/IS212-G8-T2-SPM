"use client";

import type {
  DataTableFilterableColumn,
  DataTableSearchableColumn,
} from "@/types";
import type { Table } from "@tanstack/react-table";

import { Cross2Icon } from "@radix-ui/react-icons";

import { DataTableFacetedFilter } from "@/components/data-table/data-table-faceted-filter";
// import { DataTableViewOptions } from "@/components/data-table/data-table-view-options";
import { Button, Input } from "@/components/ui";

interface DataTableToolbarProps<TData> {
  table: Table<TData>;
  filterableColumns?: DataTableFilterableColumn<TData>[];
  searchableColumns?: DataTableSearchableColumn<TData>[];
}

export function DataTableToolbar<TData>({
  table,
  filterableColumns = [],
  searchableColumns = [],
}: DataTableToolbarProps<TData>) {
  const isFiltered = table.getState().columnFilters.length > 0;
  // console.log(table.getColumn("skillRequired"));
  return (
    <div className="flex items-center justify-between py-2">
      <div className="flex flex-1 items-center space-x-2">
        {searchableColumns.length > 0 &&
          searchableColumns.map(
            (column) =>
              table.getColumn(column.id ? String(column.id) : "") && (
                <Input
                  key={String(column.id)}
                  className="h-8 w-[150px] lg:w-[250px]"
                  placeholder={`Filter ${column.title}...`}
                  value={
                    (table
                      .getColumn(String(column.id))
                      ?.getFilterValue() as string) ?? ""
                  }
                  onChange={(event) =>
                    table
                      .getColumn(String(column.id))
                      ?.setFilterValue(event.target.value)
                  }
                />
              ),
          )}
        {filterableColumns.length > 0 &&
          filterableColumns.map(
            (column) =>
              table.getColumn(column.id ? String(column.id) : "") && (
                <DataTableFacetedFilter
                  key={String(column.id)}
                  column={table.getColumn(column.id ? String(column.id) : "")}
                  data={table.getRowModel()}
                  nameColumn={table.getColumn("roleName")}
                  options={column.options}
                  title={column.title}
                />
              ),
          )}
        {isFiltered && (
          <Button
            className="h-8 px-2 lg:px-3"
            variant="ghost"
            onClick={() => table.resetColumnFilters()}
          >
            Reset
            <Cross2Icon className="ml-2 h-4 w-4" />
          </Button>
        )}
      </div>
      {/* <DataTableViewOptions table={table} /> */}
    </div>
  );
}
